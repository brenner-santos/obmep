from obmep.items import TeacherItem
from obmep.spiders import BaseTeacherSpider


class EdObmep2006TeacherSpider(BaseTeacherSpider):
    name = 'obmep2006-teacher'
    EDITION = 'obmep2006'
    start_urls = [
        'https://premiacao.obmep.org.br/2006/verRelatorioProfessoresPremiados.do.htm'
    ]

    def parse(self, response):
        for row in response.css('tbody tr'):
            data = row.css('td::text').getall()
            yield TeacherItem(
                state_code=data[1],
                city=data[2],
                teacher=data[3],
                school=data[4],
                school_type=data[5],
                group=None,
            )
