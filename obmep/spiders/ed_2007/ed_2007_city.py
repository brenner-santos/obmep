from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class EdObmep2007CitySpider(BaseCitySpider):
    name = 'obmep2007-city'
    EDITION = 'obmep2007'
    start_urls = [
        'https://premiacao.obmep.org.br/2007/verRelatorioMunicipiosPremiados.do.htm'
    ]

    def parse(self, response):
        for row in response.css('table tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(
                state_code=data[1],
                city=data[2],
            )
