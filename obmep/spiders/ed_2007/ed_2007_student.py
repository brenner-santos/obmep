from obmep.items import StudentItem
from obmep.spiders import BaseStudentSpider


class Ed2006StudentSpider(BaseStudentSpider):
    name = '2007-student'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2007/verRelatorioPremiadosGeral.do.htm'
    ]

    EDITION = 'OBMEP 2007'

    def parse(self, response):
        tables = response.css('table')

        for table in tables:
            level = table.css('font::text').get().strip()
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                yield StudentItem(
                    level=level,
                    name=data[1],
                    school=data[2],
                    school_type=data[3],
                    city=data[4],
                    state_code=data[5],
                    medal=data[6],
                    honorable_mention=data[7],
                )