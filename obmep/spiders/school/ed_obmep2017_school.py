from obmep.spiders.base.school import BaseSchoolSpider


class EdObmep2017SchoolSpider(BaseSchoolSpider):
    name = 'obmep2017-school'
    id_edition_url = '2017'
    has_private_school = True
