from obmep.spiders.base.student import BaseStudentSpider


class EdObmep2019StudentSpider(BaseStudentSpider):
    name = 'obmep2019-student'
    id_edition_url = '2019'
    has_private_school = True
