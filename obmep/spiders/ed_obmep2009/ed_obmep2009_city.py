from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class EdObmep2009CitySpider(BaseCitySpider):
    name = 'obmep2009-city'
    EDITION = 'obmep2009'
    start_urls = [
        'https://premiacao.obmep.org.br/2009/verRelatorioSecretariasEducacaoPremiados.do.htm'
    ]

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(
                state_code=data[1],
                city=data[2],
            )
