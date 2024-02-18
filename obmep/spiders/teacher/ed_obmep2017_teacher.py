from obmep.spiders.base.teacher import BaseTeacherSpider


class EdObmep2017TeacherSpider(BaseTeacherSpider):
    name = 'obmep2017-teacher'
    id_edition_url = '2017'
    has_private_school = True
