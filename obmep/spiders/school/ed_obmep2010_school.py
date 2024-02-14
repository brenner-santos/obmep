from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2010SchoolSpider(BaseSchoolSpider):
    name = 'obmep2010-school'
    start_urls = [
        'https://premiacao.obmep.org.br/2010/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        awards = [
            'Kit de material esportivo e livros/vídeos para a composição de uma biblioteca básica em Matemática e Ciências',
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
