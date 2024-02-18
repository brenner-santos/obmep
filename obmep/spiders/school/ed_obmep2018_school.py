from obmep.spiders.base.school import BaseSchoolSpider


class EdObmep2018SchoolSpider(BaseSchoolSpider):
    name = 'obmep2018-school'
    id_edition_url = '2018'
    has_private_school = True
