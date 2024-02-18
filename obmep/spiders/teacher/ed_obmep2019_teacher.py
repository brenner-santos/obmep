from obmep.spiders.base.teacher import BaseTeacherSpider


class EdObmep2019TeacherSpider(BaseTeacherSpider):
    name = 'obmep2019-teacher'
    id_edition_url = '2019'
    has_private_school = True
