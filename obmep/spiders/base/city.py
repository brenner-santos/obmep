from scrapy import Request

from obmep.items import CityItem
from obmep.spiders.base import BaseObmepSpider


class BaseCitySpider(BaseObmepSpider):
    TABLE_NAME = 'city'
    report = 'verRelatorioSecretariasEducacaoPremiados'
    awards = None

    def start_requests(self):
        edition_url = f'https://premiacao.obmep.org.br/{self.id_edition_url}/'
        yield Request(f'{edition_url}{self.report}.do.htm')

    def parse(self, response):
        awards = self.awards or self.get_awards(response)
        tables = response.css('table:has(>tbody):contains("Município")')

        for index, table in enumerate(tables):
            table_headers = self.get_table_headers(table)
            indexes = self.get_headers_indexes(table_headers)
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                yield CityItem(
                    award=awards[index],
                    name=data[indexes['name']],
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
        return [str(header.css('::text').get()).strip() for header in headers]

    def get_headers_indexes(self, table_headers):
        return {
            'name': self.index_of_substring(table_headers, 'Município'),
            'state_code': self.index_of_substring(table_headers, 'UF'),
        }

    def index_of_substring(self, input_list, substring):
        for idx, string in enumerate(input_list):
            if substring in string:
                return idx
        return -1
