from obmep.spiders.base.teacher import BaseTeacherSpider


class Ed17ObmepTeacherSpider(BaseTeacherSpider):
    name = '17obmep-teacher'
    id_edition_url = '17obmep'
    has_private_school = True
