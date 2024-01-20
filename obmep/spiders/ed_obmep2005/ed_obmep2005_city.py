import scrapy

from obmep.items import City


class EdObmep2005City(scrapy.Spider):
    name = 'EdObmep2005City'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioMunicipiosPremiados.do.htm'
    ]

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield City(
                state_code=data[1].strip(),
                city=data[2].strip(),
            )
