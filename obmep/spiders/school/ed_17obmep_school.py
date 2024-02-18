from obmep.spiders.base.school import BaseSchoolSpider


class Ed17ObmepSchoolSpider(BaseSchoolSpider):
    name = '17obmep-school'
    id_edition_url = '17obmep'
    has_private_school = True
