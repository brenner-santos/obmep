from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class Ed2008CitySpider(BaseCitySpider):
    name = '2008-city'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2008/verRelatorioSecretariasEducacaoPremiados.do.htm'
    ]

    EDITION = 'OBMEP 2008'

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(
                state_code=data[1],
                city=data[2],
            )
