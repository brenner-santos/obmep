from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2015SchoolSpider(BaseSchoolSpider):
    name = 'obmep2015-school'
    start_urls = [
        'https://premiacao.obmep.org.br/2015/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        awards = [
            'Kit esportivo',
            'Kit constituído de material didático',
            'Troféu - escolas premiadas nos anos anteriores',
            'Troféu - escolas seletivas',
        ]

        for index, table in enumerate(response.css('table')):
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()

                yield SchoolItem(
                    award=awards[index],
                    name=data[3],
                    type=data[4],
                    group=data[5],
                    city_name=data[2],
                    state_code=data[1],
                )
