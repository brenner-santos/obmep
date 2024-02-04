from obmep.items import StudentItem
from obmep.spiders import BaseStudentSpider


class EdObmep2005StudentSpider(BaseStudentSpider):
    name = 'obmep2005-student'
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioPremiadosGeral.do.htm'
    ]

    def parse(self, response):
        for table in response.css('table'):
            level = table.css('font::text').get()
            for row in table.css('tbody tr'):
                data = row.css('td::text').getall()
                is_medalist = data[6] != '---'
                yield StudentItem(
                    award=data[6] if is_medalist else 'Menção Honrosa',
                    name=data[1],
                    level=level,
                    school={
                        'name': data[2],
                        'type': data[3],
                        'city_name': data[4],
                        'state_code': data[5],
                    },
                )
