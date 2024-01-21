import scrapy
from scrapy.exceptions import NotConfigured


class BaseObmepSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super(BaseObmepSpider, self).__init__(*args, **kwargs)

        if not hasattr(self, 'EDITION'):
            raise NotConfigured('Please set a value for `EDITION`')


class BaseCitySpider(BaseObmepSpider):
    TABLE_NAME = 'city'


class BaseSchoolSpider(BaseObmepSpider):
    TABLE_NAME = 'school'


class BaseStudentSpider(BaseObmepSpider):
    TABLE_NAME = 'student'


class BaseTeacherSpider(BaseObmepSpider):
    TABLE_NAME = 'teacher'
