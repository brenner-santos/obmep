from obmep.spiders.base.school import BaseSchoolSpider


class EdObmep2005SchoolSpider(BaseSchoolSpider):
    name = 'obmep2005-school'
    id_edition_url = '2005'
    awards = [
        'Laboratório de Computação',
        'Certificado de Mérito Nacional',
    ]
