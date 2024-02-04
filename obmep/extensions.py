import json

from scrapy import signals
from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import JSON, DateTime, Integer, Numeric, String

Base = declarative_base()


class JobStats(Base):
    __tablename__ = 'job_stats'
    id = Column(Integer, primary_key=True)
    spider = Column(String)
    start_time = Column(DateTime)
    elapsed_time_seconds = Column(Numeric)
    item_scraped_count = Column(Integer)
    job_stats = Column(JSON)


class StatsPersist:
    def __init__(self, crawler, database_url):
        self._stats = crawler.stats
        self._database_url = database_url

    @classmethod
    def from_crawler(cls, crawler):
        database_url = crawler.settings.get('OBMEP_DATABASE_URL')

        o = cls(crawler, database_url)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

    def spider_opened(self, spider):
        engine = create_engine(self._database_url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def spider_closed(self, spider, reason):
        stats = self._stats.get_stats()
        if not 'item_scraped_count' in stats:
            stats['item_scraped_count'] = 0

        serializable_stats = json.loads(json.dumps(stats, default=str))

        job_stats = JobStats(
            spider=spider.name,
            start_time=stats['start_time'],
            elapsed_time_seconds=stats['elapsed_time_seconds'],
            item_scraped_count=stats['item_scraped_count'],
            job_stats=serializable_stats,
        )
        session = self.Session()
        session.add(job_stats)
        session.commit()
