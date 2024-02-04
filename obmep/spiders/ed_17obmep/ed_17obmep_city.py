from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class Ed17ObmepCitySpider(BaseCitySpider):
    name = '17obmep-city'
    start_urls = [
        'https://premiacao.obmep.org.br/17obmep/verRelatorioSecretariasEducacaoPremiados.do.htm'
    ]

    def parse(self, response):
        awards = ['Troféu']

        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(award=awards[0], name=data[1], state_code=data[0])
