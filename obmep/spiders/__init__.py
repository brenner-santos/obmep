import scrapy
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings


class BaseObmepSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super(BaseObmepSpider, self).__init__(*args, **kwargs)

        if not hasattr(self, 'EDITION'):
            raise NotConfigured('Please set a value for `EDITION`')


class BaseCitySpider(BaseObmepSpider):
    TABLE_NAME = 'city'
    custom_settings = {
        'ITEM_PIPELINES': {
            'obmep.pipelines.ProcessCityPipeline': 100,
            **get_project_settings().get('ITEM_PIPELINES'),
        },
    }


class BaseSchoolSpider(BaseObmepSpider):
    TABLE_NAME = 'school'
    custom_settings = {
        'ITEM_PIPELINES': {
            'obmep.pipelines.ProcessSchoolPipeline': 100,
            **get_project_settings().get('ITEM_PIPELINES'),
        },
    }


class BaseStudentSpider(BaseObmepSpider):
    TABLE_NAME = 'student'
    custom_settings = {
        'ITEM_PIPELINES': {
            'obmep.pipelines.ProcessStudentPipeline': 100,
            **get_project_settings().get('ITEM_PIPELINES'),
        },
    }


class BaseTeacherSpider(BaseObmepSpider):
    TABLE_NAME = 'teacher'
    custom_settings = {
        'ITEM_PIPELINES': {
            'obmep.pipelines.ProcessTeacherPipeline': 100,
            **get_project_settings().get('ITEM_PIPELINES'),
        },
    }
