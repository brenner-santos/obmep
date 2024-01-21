from sqlalchemy.orm import sessionmaker

from obmep.models import Base, create_table, db_connect


class DefaultValuesPipeline:
    def process_item(self, item, spider):
        item['edition'] = getattr(spider, 'EDITION')

        return item


class SQLDatabasePipeline:
    def open_spider(self, spider):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        table_name = getattr(spider, 'TABLE_NAME')
        fields = Base.metadata.tables[table_name].columns.keys()
        values = {field: item.get(field) for field in fields}
        stmt = Base.metadata.tables[table_name].insert().values(**values)

        try:
            session.execute(stmt)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
