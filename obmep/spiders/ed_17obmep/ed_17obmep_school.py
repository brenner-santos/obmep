from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class Ed17ObmepSchoolSpider(BaseSchoolSpider):
    name = '17obmep-school'
    start_urls = [
        'https://premiacao.obmep.org.br/17obmep/verRelatorioEscolasPremiadas.do.htm',
        'https://premiacao.obmep.org.br/17obmep/verRelatorioEscolasPremiadas.privada.do.htm',
    ]

    def parse(self, response):
        awards = [
            award.split('-')[0][8:]
            for award in response.css('b:contains("Prêmio")::text').getall()
        ]

        for index, table in enumerate(response.css('table')):
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                yield SchoolItem(
                    award=awards[index],
                    name=data[2],
                    type=data[3],
                    group=data[4],
                    city_name=data[1],
                    state_code=data[0],
                )
