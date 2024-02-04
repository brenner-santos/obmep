from obmep.items import StudentItem
from obmep.spiders import BaseStudentSpider


class EdObmep2006StudentSpider(BaseStudentSpider):
    name = 'obmep2006-student'
    EDITION = 'obmep2006'
    start_urls = [
        f'http://premiacao.obmep.org.br/2006/verRelatorioPremiadosGeral-{code}.do.htm'
        for code in BaseStudentSpider.STATES_CODE
    ]

    def parse(self, response):
        tables = response.css('table')

        for table in tables:
            level = table.css('font::text').get()
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
