from obmep.spiders.base.school import BaseSchoolSpider


class Ed18ObmepSchoolSpider(BaseSchoolSpider):
    name = '18obmep-school'
    id_edition_url = '18obmep'
    has_private_school = True
