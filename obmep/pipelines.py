import datetime as dt

from sqlalchemy.orm import sessionmaker

from obmep.models import Base, create_table, db_connect


class DefaultValuesPipeline:
    def open_spider(self, spider):
        self.created_at = dt.datetime.utcnow()

    def process_item(self, item, spider):
        item['edition'] = getattr(spider, 'EDITION')
        item['created_at'] = self.created_at

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


class ProcessCityPipeline:
    def process_item(self, item, spider):
        item['state_code'] = item['state_code'].strip()
        item['city'] = item['city'].strip()

        return item


class ProcessSchoolPipeline:
    def process_item(self, item, spider):
        item['state_code'] = item['state_code'].strip()
        item['city'] = item['city'].strip()
        item['school'] = item['school'].strip()
        item['school_type'] = item['school_type'].strip()
        item['group'] = item['group'].strip() if item['group'] else None

        return item


class ProcessStudentPipeline:
    def process_item(self, item, spider):
        item['level'] = int(item['level'].strip()[-1])
        item['name'] = item['name'].strip()
        item['city'] = item['city'].strip()
        item['state_code'] = item['state_code'].strip()
        item['school'] = item['school'].strip()
        item['school_type'] = item['school_type'].strip()
        item['medal'] = item['medal'].strip()
        item['medal'] = None if item['medal'] == '---' else item['medal']
        item['honorable_mention'] = item['honorable_mention'].strip() == 'Sim'

        return item


class ProcessTeacherPipeline:
    def process_item(self, item, spider):
        item['state_code'] = item['state_code'].strip()
        item['city'] = item['city'].strip()
        item['teacher'] = item['teacher'].strip()
        item['school'] = item['school'].strip()
        item['school_type'] = item['school_type'].strip()
        if item['group']:
            item['group'] = int(item['group'].strip().split(' ')[-1])
        else:
            item['group'] = None

        return item
