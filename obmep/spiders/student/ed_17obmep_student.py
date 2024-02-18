from obmep.spiders.base.student import BaseStudentSpider


class Ed17ObmepStudentSpider(BaseStudentSpider):
    name = '17obmep-student'
    id_edition_url = '17obmep'
    has_private_school = True
