from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class Ed17obmepCitySpider(BaseCitySpider):
    name = '17obmep-city'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/17obmep/verRelatorioSecretariasEducacaoPremiados.do.htm'
    ]

    EDITION = '17ª OBMEP'

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(
                state_code=data[0],
                city=data[1],
            )
