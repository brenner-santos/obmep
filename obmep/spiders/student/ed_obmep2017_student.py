from obmep.spiders.base.student import BaseStudentSpider


class EdObmep2017StudentSpider(BaseStudentSpider):
    name = 'obmep2017-student'
    id_edition_url = '2017'
    has_private_school = True
