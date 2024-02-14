import json

from obmep.items import TeacherItem
from obmep.spiders import BaseTeacherSpider


class EdObmep2007TeacherSpider(BaseTeacherSpider):
    name = 'obmep2007-teacher'
    start_urls = [
        'https://premiacao.obmep.org.br/2007/verRelatorioProfessoresPremiados.do.htm'
    ]

    def parse(self, response):
        awards = ['Estágio no IMPA']

        for row in response.css('tbody tr'):
            data = row.css('td::text').getall()
            yield TeacherItem(
                award=awards[0],
                name=data[3],
                group=None,
                schools=[
                    {
                        'name': data[4],
                        'type': data[5],
                        'city_name': data[2],
                        'state_code': data[1],
                    }
                ],
            )
