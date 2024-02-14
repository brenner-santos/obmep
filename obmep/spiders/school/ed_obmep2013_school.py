from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2013SchoolSpider(BaseSchoolSpider):
    name = 'obmep2013-school'
    start_urls = [
        'https://premiacao.obmep.org.br/2013/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        awards = [
            '1 (um) kit esportivo',
            '1 (um) diploma e 1 (um) kit constituído de material didático',
            'Troféu',
        ]

        for index, table in enumerate(response.css('table')):
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()

                if len(data) == 6:
                    yield SchoolItem(
                        award=awards[index],
                        name=data[4],
                        type=data[5],
                        group=data[1],
                        city_name=data[3],
                        state_code=data[2],
                    )
                elif len(data) == 5:
                    yield SchoolItem(
                        award=awards[index],
                        name=data[3],
                        type=data[4],
                        group=None,
                        city_name=data[2],
                        state_code=data[1],
                    )
