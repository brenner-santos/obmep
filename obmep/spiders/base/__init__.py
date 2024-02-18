import csv

from scrapy import Spider
from scrapy.exceptions import NotConfigured


def load_csv_column(file_path, column_name):
    with open(file_path) as f:
        csv_reader = csv.DictReader(f)
        return [row[column_name] for row in csv_reader]


class BaseObmepSpider(Spider):
    allowed_domains = ['premiacao.obmep.org.br']
    TABLE_NAME = ''
    EDITIONS_CODE = load_csv_column(
        'obmep/resources/editions.csv', 'cd_edition'
    )
    STATES_CODE = load_csv_column('obmep/resources/states.csv', 'cd_state')

    def __init__(self, *args, **kwargs):
        super(BaseObmepSpider, self).__init__(*args, **kwargs)

        self.check_configuration()

    def check_configuration(self):
        edition_code, table = getattr(self, 'name').split('-', 1)

        if table != self.TABLE_NAME:
            raise NotConfigured(
                'Please define `name` according to the structure: <edition-code>-<table>'
            )

        if edition_code not in self.EDITIONS_CODE:
            raise NotConfigured(
                'Edition code not found in the editions CSV file. Please check your `name` configuration.'
            )
