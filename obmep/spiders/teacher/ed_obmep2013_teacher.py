from obmep.items import TeacherItem
from obmep.spiders import BaseTeacherSpider


class EdObmep2013TeacherSpider(BaseTeacherSpider):
    name = 'obmep2013-teacher'
    start_urls = [
        'https://premiacao.obmep.org.br/2013/verRelatorioProfessoresPremiados.do.htm'
    ]

    def parse(self, response):
        awards = [
            ' '.join(award.css('::text').getall())[8:]
            for award in response.css('b:contains("Prêmio")')
        ]

        for index, table in enumerate(response.css('table')):
            for row in table.css('tbody tr'):
                data = row.css('td')

                if len(data) == 7:
                    school_names = self.remove_dash(
                        data[5].css('::text').getall()
                    )
                    school_types = self.remove_dash(
                        data[6].css('::text').getall()
                    )
                    cities = self.remove_dash(data[3].css('::text').getall())
                    state_codes = self.remove_dash(
                        data[2].css('::text').getall()
                    )

                    yield TeacherItem(
                        award=awards[index],
                        name=data[4].css('::text').get(),
                        group=data[1].css('::text').get(),
                        schools=self.extract_schools(
                            school_names, school_types, cities, state_codes
                        ),
                    )

                elif len(data) == 6:
                    school_names = self.remove_dash(
                        data[4].css('::text').getall()
                    )
                    school_types = self.remove_dash(
                        data[5].css('::text').getall()
                    )
                    cities = self.remove_dash(data[2].css('::text').getall())
                    state_codes = self.remove_dash(
                        data[1].css('::text').getall()
                    )

                    yield TeacherItem(
                        award=awards[index],
                        name=data[3].css('::text').get(),
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
