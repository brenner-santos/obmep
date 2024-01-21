from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class EdObmep2005SchoolSpider(BaseSchoolSpider):
    name = 'obmep_2005-school'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioEscolasPremiadas.do.htm'
    ]

    EDITION = 'OBMEP 2005'

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield SchoolItem(
                state_code=data[1],
                city=data[2],
                school=data[3],
                school_type=data[4],
                group=None,
            )
