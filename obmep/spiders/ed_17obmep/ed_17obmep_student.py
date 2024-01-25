import scrapy

from obmep.items import StudentItem
from obmep.spiders import BaseStudentSpider


class Ed17obmepStudentSpider(BaseStudentSpider):
    name = '17obmep-student'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = ['http://premiacao.obmep.org.br/17obmep/mapa.htm']

    EDITION = '17ª OBMEP'

    def parse(self, response):
        report = 'verRelatorioPremiadosGeral'
        for code in self.STATES_CODE:
            yield scrapy.Request(
                response.urljoin(f'{report}-{code}.do.htm'),
                callback=self.parse_student,
            )
            yield scrapy.Request(
                response.urljoin(f'{report}-{code}.privada.do.htm'),
                callback=self.parse_student,
            )

    def parse_student(self, response):
        tables = response.css('table')

        for table in tables:
            level = table.css('font::text').get().strip()
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                if data[0] == 'Não existem registros de alunos neste Nível.':
                    continue

                yield StudentItem(
                    level=level,
                    name=data[0],
                    school=data[1],
                    school_type=data[2],
                    city=data[3],
                    state_code=data[4],
                    medal=data[5],
                    honorable_mention=data[6],
                )
