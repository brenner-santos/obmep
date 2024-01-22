import scrapy
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings


class BaseObmepSpider(scrapy.Spider):
    STATES_CODE = [
        'AC',
        'AL',
        'AM',
        'AP',
        'BA',
        'CE',
        'DF',
        'ES',
        'GO',
        'MA',
        'MG',
        'MS',
        'MT',
        'PA',
        'PB',
        'PE',
        'PI',
        'PR',
        'RJ',
        'RN',
        'RO',
        'RR',
        'RS',
        'SC',
        'SE',
        'SP',
        'TO',
    ]

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
