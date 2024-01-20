import scrapy

from obmep.items import Teacher


class EdObmep2005Teacher(scrapy.Spider):
    name = 'EdObmep2005Teacher'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioProfessoresPremiados.do.htm'
    ]

    def parse(self, response):
        for row in response.css('tbody tr'):
            data = row.css('td::text').getall()
            yield Teacher(
                state_code=data[1].strip(),
                city=data[2].strip(),
                teacher=data[3].strip(),
                school=data[4].strip(),
                school_type=data[5].strip(),
                group=None,
            )
