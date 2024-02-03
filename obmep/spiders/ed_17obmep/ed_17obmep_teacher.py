from obmep.items import TeacherItem
from obmep.spiders import BaseTeacherSpider


class Ed17ObmepTeacherSpider(BaseTeacherSpider):
    name = '17obmep-teacher'
    EDITION = '17obmep'
    start_urls = [
        'https://premiacao.obmep.org.br/17obmep/verRelatorioProfessoresPremiados.do.htm',
        'https://premiacao.obmep.org.br/17obmep/verRelatorioProfessoresPremiados.privada.do.htm',
    ]

    def parse(self, response):
        for row in response.css('tbody tr'):
            data = row.css('td')
            for school_idx in range(len(data[3].css('::text').getall())):
                if data[3].css('::text')[school_idx].get() == '-':
                    continue

                if school_idx >= len(data[4].getall()):
                    school_type = data[4].css('::text')[-1].get()
                else:
                    school_type = data[4].css('::text')[school_idx].get()

                if school_idx >= len(data[1].getall()):
                    city = data[1].css('::text')[-1].get()
                else:
                    city = data[1].css('::text')[school_idx].get()

                if school_idx >= len(data[0].getall()):
                    state_code = data[0].css('::text')[-1].get()
                else:
                    state_code = data[0].css('::text')[school_idx].get()

                yield TeacherItem(
                    state_code=state_code,
                    city=city,
                    teacher=data[2].css('::text').get(),
                    school=data[3].css('::text')[school_idx].get(),
                    school_type=school_type,
                    group=data[5].css('::text').get(),
                )
