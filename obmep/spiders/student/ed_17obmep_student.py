from scrapy import Request

from obmep.items import StudentItem
from obmep.spiders import BaseStudentSpider


class Ed17ObmepStudentSpider(BaseStudentSpider):
    name = '17obmep-student'

    def start_requests(self):
        url = (
            'http://premiacao.obmep.org.br/17obmep/verRelatorioPremiadosGeral'
        )
        for code in self.STATES_CODE:
            yield Request(f'{url}-{code}.do.htm')
            yield Request(f'{url}-{code}.privada.do.htm')

    def parse(self, response):
        for table in response.css('table'):
            level = table.css('font::text').get()
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                if data[0] == 'Não existem registros de alunos neste Nível.':
                    continue
                is_medalist = data[5] != '---'
                yield StudentItem(
                    award=data[5] if is_medalist else 'Menção Honrosa',
                    name=data[0],
                    level=level,
                    school={
                        'name': data[1],
                        'type': data[2],
                        'city_name': data[3],
                        'state_code': data[4],
                    },
                )
