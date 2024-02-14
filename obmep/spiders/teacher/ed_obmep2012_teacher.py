from obmep.items import TeacherItem
from obmep.spiders import BaseTeacherSpider


class EdObmep2012TeacherSpider(BaseTeacherSpider):
    name = 'obmep2012-teacher'
    start_urls = [
        'https://premiacao.obmep.org.br/2012/verRelatorioProfessoresPremiados.do.htm'
    ]

    def parse(self, response):
        awards = [
            ' '.join(award.css('::text').getall()).split('-')[0][8:]
            for award in response.css('b:contains("Prêmio")')
        ]

        table = response.css('table:first-of-type')
        for row in table.css('tbody tr'):
            data = row.css('td')

            school_names = self.remove_dash(data[4].css('::text').getall())
            school_types = [name.strip()[-2:-1] for name in school_names]
            school_names = [name.strip()[:-3] for name in school_names]
            cities = self.remove_dash(data[2].css('::text').getall())
            state_codes = self.remove_dash(data[1].css('::text').getall())

            yield TeacherItem(
                award=awards[0],
                name=data[3].css('::text').get(),
                group=None,
                schools=self.extract_schools(
                    school_names, school_types, cities, state_codes
                ),
            )

        table = response.css('table:last-of-type')
        for row in table.css('tbody tr'):
            data = row.css('td')

            school_names = self.remove_dash(data[3].css('::text').getall())
            school_types = [name.strip()[-2:-1] for name in school_names]
            school_names = [name.strip()[:-3] for name in school_names]
            cities = self.remove_dash(data[1].css('::text').getall())
            state_codes = [city.strip()[-2:] for city in cities]
            cities = [city.strip()[:-4] for city in cities]

            yield TeacherItem(
                award=awards[-1],
                name=data[2].css('::text').get(),
                group=None,
                schools=self.extract_schools(
                    school_names, school_types, cities, state_codes
                ),
            )

    def extract_schools(self, names, types, cities, state_codes):
        keys = ['name', 'type', 'city_name', 'state_code']

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
