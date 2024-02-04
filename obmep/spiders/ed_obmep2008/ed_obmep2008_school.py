from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2008SchoolSpider(BaseSchoolSpider):
    name = 'obmep2008-school'
    start_urls = [
        'https://premiacao.obmep.org.br/2008/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        awards = [
            'Kit para exibição audiovisual e livros para a composição de uma biblioteca básica em Matemática e Ciências',
            'Troféu',
            'Livros para a composição de uma biblioteca básica em Matemática e Ciências',
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
