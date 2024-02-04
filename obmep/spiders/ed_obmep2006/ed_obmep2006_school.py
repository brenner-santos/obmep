from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2006SchoolSpider(BaseSchoolSpider):
    name = 'obmep2006-school'
    EDITION = 'obmep2006'
    start_urls = [
        'https://premiacao.obmep.org.br/2006/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        for row in response.css('table tbody tr'):
            data = row.css('td::text').getall()
            yield SchoolItem(
                state_code=data[1],
                city=data[2],
                school=data[3],
                school_type=data[4],
                group=None,
            )
