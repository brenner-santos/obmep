from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2006SchoolSpider(BaseSchoolSpider):
    name = 'obmep2006-school'
    start_urls = [
        'https://premiacao.obmep.org.br/2006/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        awards = [
            'Notebook c/ kit de projeção móvel (datashow) e livros para a composição de uma biblioteca básica em Matemática',
            'Livros para a composição de uma biblioteca básica em Matemática',
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
