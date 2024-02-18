from obmep.spiders.base.student import BaseStudentSpider


class Ed16ObmepStudentSpider(BaseStudentSpider):
    name = '16obmep-student'
    id_edition_url = '16aobmep'
    has_private_school = True
