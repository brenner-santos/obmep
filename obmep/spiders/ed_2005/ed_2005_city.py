from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class EdObmep2005CitySpider(BaseCitySpider):
    name = 'obmep2005-city'
    EDITION = 'obmep2005'
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioMunicipiosPremiados.do.htm'
    ]

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(
                state_code=data[1],
                city=data[2],
            )
