from obmep.spiders.base.school import BaseSchoolSpider


class EdObmep2019SchoolSpider(BaseSchoolSpider):
    name = 'obmep2019-school'
    id_edition_url = '2019'
    has_private_school = True
