from scrapy import Request

from obmep.items import StudentItem
from obmep.spiders.base import BaseObmepSpider


class BaseStudentSpider(BaseObmepSpider):
    TABLE_NAME = 'student'
    report = 'verRelatorioPremiadosGeral'
    has_private_school = False

    def start_requests(self):
        edition_url = f'https://premiacao.obmep.org.br/{self.id_edition_url}/'
        for code in self.STATES_CODE:
            yield Request(f'{edition_url}{self.report}-{code}.do.htm')

        if self.has_private_school:
            for code in self.STATES_CODE:
                yield Request(
                    f'{edition_url}{self.report}-{code}.privada.do.htm'
                )

    def parse(self, response):
        for table in response.css('table'):
            level = table.css('font::text').get()
            table_headers = self.get_table_headers(table)
            indexes = self.get_headers_indexes(table_headers)
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                if self.has_awards(data):
                    yield StudentItem(
                        award=self.get_award(data[indexes['medal']]),
                        name=data[indexes['name']],
                        level=level,
                        school={
                            'name': data[indexes['school_name']],
                            'type': data[indexes['school_type']],
                            'city_name': data[indexes['city_name']],
                            'state_code': data[indexes['state_code']],
                        },
                    )

    def has_awards(self, data):
        return data[0] != 'Não existem registros de alunos neste Nível.'

    def get_award(self, medal):
        return medal if medal != '---' else 'Menção Honrosa'

    def get_table_headers(self, table):
        headers = table.css('tr:last-child th')
        return [str(header.css('::text').get()).strip() for header in headers]

    def get_headers_indexes(self, table_headers):
        return {
            'name': self.index_of_substring(table_headers, 'Nome'),
            'school_name': self.index_of_substring(table_headers, 'Escola'),
            'school_type': self.index_of_substring(table_headers, 'Tipo'),
            'city_name': self.index_of_substring(table_headers, 'Município'),
            'state_code': self.index_of_substring(table_headers, 'UF'),
            'medal': self.index_of_substring(table_headers, 'Medalha'),
        }

    def index_of_substring(self, input_list, substring):
        for idx, string in enumerate(input_list):
            if substring in string:
                return idx
        return -1
