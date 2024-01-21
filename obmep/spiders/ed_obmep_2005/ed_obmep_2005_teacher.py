from obmep.items import TeacherItem
from obmep.spiders import BaseTeacherSpider


class EdObmep2005TeacherSpider(BaseTeacherSpider):
    name = 'obmep_2005-teacher'
    allowed_domains = ['premiacao.obmep.org.br']
    start_urls = [
        'https://premiacao.obmep.org.br/2005/verRelatorioProfessoresPremiados.do.htm'
    ]

    EDITION = 'OBMEP 2005'

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
