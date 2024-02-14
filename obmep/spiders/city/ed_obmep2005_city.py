from obmep.items import CityItem
from obmep.spiders import BaseCitySpider


class EdObmep2005CitySpider(BaseCitySpider):
    name = 'obmep2005-city'
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioMunicipiosPremiados.do.htm'
    ]

    def parse(self, response):
        awards = ['Quadras de Esporte', 'Certificado de Mérito Nacional']

        for row in response.css('table:first-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(award=awards[0], name=data[2], state_code=data[3])

        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield CityItem(award=awards[1], name=data[2], state_code=data[1])
