from obmep.items import StudentItem
from obmep.spiders import BaseStudentSpider


class EdObmep2005StudentSpider(BaseStudentSpider):
    name = 'obmep_2005-student'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioPremiadosGeral.do.htm'
    ]

    EDITION = 'OBMEP 2005'

    def parse(self, response):
        tables = response.css('table')

        for table in tables:
            level = table.css('font::text').get().strip()
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                yield StudentItem(
                    level=level,
                    name=data[1].strip(),
                    school=data[2].strip(),
                    school_type=data[3].strip(),
                    city=data[4].strip(),
                    state_code=data[5].strip(),
                    medal=data[6].strip(),
                    honorable_mention=data[7].strip(),
                )
