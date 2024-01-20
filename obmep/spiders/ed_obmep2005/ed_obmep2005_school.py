import scrapy


class EdObmep2005School(scrapy.Spider):
    name = 'EdObmep2005School'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioEscolasPremiadas.do.htm'
    ]

    def parse(self, response):
        for row in response.css('table:last-of-type tbody tr'):
            data = row.css('td::text').getall()
            yield {
                'state_code': data[1].strip(),
                'city': data[2].strip(),
                'school': data[3].strip(),
                'school_type': data[4].strip(),
            }
