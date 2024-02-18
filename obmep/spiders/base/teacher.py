from scrapy import Request

from obmep.items import TeacherItem
from obmep.spiders.base import BaseObmepSpider


class BaseTeacherSpider(BaseObmepSpider):
    TABLE_NAME = 'teacher'
    report = 'verRelatorioProfessoresPremiados'
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
                data = row.css('td')
                yield TeacherItem(
                    award=awards[index],
                    name=data[indexes['name']].css('::text').get(),
                    group=data[indexes['group']].css('::text').get()
                    if indexes['group'] != -1
                    else None,
                    schools=self.extract_schools(data, indexes),
                )

    def extract_schools(self, data, indexes):
        names = data[indexes['school_name']].css('::text').getall()
        cities = data[indexes['city_name']].css('::text').getall()

        names = self.remove_dash(names)
        cities = self.remove_dash(cities)

        if indexes['school_type'] != indexes['school_name']:
            types = data[indexes['school_type']].css('::text').getall()
            types = self.remove_dash(types)
        else:
            types = [name.strip()[-2:-1] for name in names]
            names = [name.strip()[:-3] for name in names]

        if indexes['state_code'] != -1:
            state_codes = data[indexes['state_code']].css('::text').getall()
            state_codes = self.remove_dash(state_codes)
        else:
            state_codes = [city.strip()[-2:] for city in cities]
            cities = [city.strip()[:-4] for city in cities]

        types = self.fill(types, len(names))
        cities = self.fill(cities, len(names))
        state_codes = self.fill(state_codes, len(names))

        return [
            dict(zip(['name', 'type', 'city_name', 'state_code'], values))
            for values in zip(names, types, cities, state_codes)
        ]

    def remove_dash(self, data_list):
        return list(filter(lambda data: data != '-', data_list))

    def fill(self, data_list, size=0):
        if size <= len(data_list):
            return data_list[:size]
        last_value = data_list[-1]
        return data_list + [last_value] * (size - len(data_list))

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
            'name': self.index_of_substring(table_headers, 'Professor'),
            'school_name': self.index_of_substring(table_headers, 'Escola'),
            'school_type': self.index_of_substring(table_headers, 'Tipo'),
            'group': self.index_of_substring(table_headers, 'Grupo'),
            'city_name': self.index_of_substring(table_headers, 'Município'),
            'state_code': self.index_of_substring(table_headers, 'UF'),
        }

    def index_of_substring(self, input_list, substring):
        for idx, string in enumerate(input_list):
            if substring in string:
                return idx
        return -1
