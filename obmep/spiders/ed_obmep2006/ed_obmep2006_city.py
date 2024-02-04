from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class EdObmep2006CitySpider(BaseCitySpider):
    name = 'obmep2006-city'
    start_urls = [
        'https://premiacao.obmep.org.br/2006/verRelatorioMunicipiosPremiados.do.htm'
    ]

    def parse(self, response):
        awards = ['Quadras de Esporte', 'Troféu']

        for row in response.css('table:first-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(award=awards[0], name=data[2], state_code=data[3])

        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(award=awards[1], name=data[2], state_code=data[1])
