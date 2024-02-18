from scrapy import Request

from obmep.items import SchoolItem
from obmep.spiders.base import BaseObmepSpider


class BaseSchoolSpider(BaseObmepSpider):
    TABLE_NAME = 'school'
    report = 'verRelatorioEscolasPremiadas'
    has_private_school = False
    awards = None

    def start_requests(self):
        edition_url = f'https://premiacao.obmep.org.br/{self.id_edition_url}/'
        yield Request(f'{edition_url}{self.report}.do.htm')
        if self.has_private_school:
            yield Request(f'{edition_url}{self.report}.privada.do.htm')

    def parse(self, response):
        awards = self.awards or self.get_awards(response)
        for index, table in enumerate(response.css('table')):
            table_headers = self.get_table_headers(table)
            indexes = self.get_headers_indexes(table_headers)
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                yield SchoolItem(
                    award=awards[index],
                    name=data[indexes['name']],
                    type=data[indexes['type']],
                    group=data[indexes['group']] if indexes['group'] else None,
                    city_name=data[indexes['city_name']],
                    state_code=data[indexes['state_code']],
                )

    def get_awards(self, response):
        awards = response.css('b:contains("Prêmio")')
        awards_formatted = []
        for award in awards:
            award = ' '.join(award.css('::text').getall())
            award = ' '.join(award.split())
            award = award.split(':', 1)[1].strip()
            awards_formatted.append(award)
        return awards_formatted

    def get_table_headers(self, table):
        headers = table.css('tr:last-child th')
        if len(headers) == 0:
            headers = table.css('th')
        return [str(header.css('::text').get()).strip() for header in headers]

    def get_headers_indexes(self, table_headers):
        return {
            'name': self.index_of_substring(table_headers, 'Escola'),
            'type': self.index_of_substring(table_headers, 'Tipo'),
            'group': self.index_of_substring(table_headers, 'Grupo'),
            'city_name': self.index_of_substring(table_headers, 'Município'),
            'state_code': self.index_of_substring(table_headers, 'UF'),
        }

    def index_of_substring(self, input_list, substring):
        for idx, string in enumerate(input_list):
            if substring in string:
                return idx
        return -1
