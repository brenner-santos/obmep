from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2012SchoolSpider(BaseSchoolSpider):
    name = 'obmep2012-school'
    start_urls = [
        'https://premiacao.obmep.org.br/2012/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        awards = [
            '1 (um) computador, com pacote de programas livres relacionados ao ensino de matemática e uma impressora',
            'Troféu',
        ]

        for index, table in enumerate(response.css('table')):
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                yield SchoolItem(
                    award=awards[index],
                    name=data[3],
                    type=data[4],
                    group=None,
                    city_name=data[2],
                    state_code=data[1],
                )
