from obmep.spiders.base.teacher import BaseTeacherSpider


class EdObmep2018TeacherSpider(BaseTeacherSpider):
    name = 'obmep2018-teacher'
    id_edition_url = '2018'
    has_private_school = True
