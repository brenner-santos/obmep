from obmep.spiders.base.student import BaseStudentSpider


class EdObmep2018StudentSpider(BaseStudentSpider):
    name = 'obmep2018-student'
    id_edition_url = '2018'
    has_private_school = True
