from obmep.spiders.base.school import BaseSchoolSpider


class Ed16ObmepSchoolSpider(BaseSchoolSpider):
    name = '16obmep-school'
    id_edition_url = '16aobmep'
    has_private_school = True
