from obmep.spiders.base.teacher import BaseTeacherSpider


class Ed16ObmepTeacherSpider(BaseTeacherSpider):
    name = '16obmep-teacher'
    id_edition_url = '16aobmep'
    has_private_school = True
