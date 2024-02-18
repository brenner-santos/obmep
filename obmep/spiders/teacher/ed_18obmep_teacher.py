from obmep.spiders.base.teacher import BaseTeacherSpider


class Ed18ObmepTeacherSpider(BaseTeacherSpider):
    name = '18obmep-teacher'
    id_edition_url = '18obmep'
    has_private_school = True
