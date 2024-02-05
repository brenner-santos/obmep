from obmep.items import TeacherItem
from obmep.spiders import BaseTeacherSpider


class EdObmep2011TeacherSpider(BaseTeacherSpider):
    name = 'obmep2011-teacher'
    start_urls = [
        'https://premiacao.obmep.org.br/2011/verRelatorioProfessoresPremiados.do.htm'
    ]

    def parse(self, response):
        awards = [
            ' '.join(award.css('::text').getall()).split('-')[0][8:]
            for award in response.css('b:contains("Prêmio")')
        ]

        for index, table in enumerate(response.css('table')):
            for row in table.css('tbody tr'):
                data = row.css('td')
                yield TeacherItem(
                    award=awards[index],
                    name=data[3].css('::text').get(),
                    group=None,
                    schools=self.extract_schools(data),
                )

    def extract_schools(self, data):
        keys = ['name', 'type', 'city_name', 'state_code']

        names = self.remove_dash(data[4].css('::text').getall())
        cities = self.remove_dash(data[2].css('::text').getall())
        state_codes = self.remove_dash(data[1].css('::text').getall())

        types = [name[-2:-1] for name in names]
        names = [name[:-3] for name in names]

        types = self.fill(types, len(names))
        cities = self.fill(cities, len(names))
        state_codes = self.fill(state_codes, len(names))

        return [
            dict(zip(keys, values))
            for values in zip(names, types, cities, state_codes)
        ]

    def remove_dash(self, data_list):
        return list(filter(lambda data: data != '-', data_list))

    def fill(self, data_list, size=0):
        if size <= len(data_list):
            return data_list[:size]
        last_value = data_list[-1]
        return data_list + [last_value] * (size - len(data_list))
