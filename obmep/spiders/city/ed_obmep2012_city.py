from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class EdObmep2012CitySpider(BaseCitySpider):
    name = 'obmep2012-city'
    start_urls = [
        'https://premiacao.obmep.org.br/2012/verRelatorioSecretariasEducacaoPremiados.do.htm'
    ]

    def parse(self, response):
        awards = ['Troféu']

        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(award=awards[0], name=data[2], state_code=data[1])
