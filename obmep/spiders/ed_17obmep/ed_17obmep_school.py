from obmep.items import SchoolItem
from obmep.spiders import BaseSchoolSpider


class Ed17obmepSchoolSpider(BaseSchoolSpider):
    name = '17obmep-school'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/17obmep/verRelatorioEscolasPremiadas.do.htm',
        'https://premiacao.obmep.org.br/17obmep/verRelatorioEscolasPremiadas.privada.do.htm',
    ]

    EDITION = '17ª OBMEP'

    def parse(self, response):
        for row in response.css('table tbody tr'):
            data = row.css('td::text').getall()
            yield SchoolItem(
                state_code=data[0],
                city=data[1],
                school=data[2],
                school_type=data[3],
                group=data[4],
            )
