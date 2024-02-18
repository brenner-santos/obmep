from obmep.spiders.base.student import BaseStudentSpider


class Ed18ObmepStudentSpider(BaseStudentSpider):
    name = '18obmep-student'
    id_edition_url = '18obmep'
    has_private_school = True
