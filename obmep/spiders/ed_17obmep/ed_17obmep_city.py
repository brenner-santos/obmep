from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class Ed17ObmepCitySpider(BaseCitySpider):
    name = '17obmep-city'
    EDITION = '17obmep'
    start_urls = [
        'https://premiacao.obmep.org.br/17obmep/verRelatorioSecretariasEducacaoPremiados.do.htm'
    ]

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(
                state_code=data[0],
                city=data[1],
            )
