from obmep.items import SchoolItem
from obmep.spiders.base.school import BaseSchoolSpider


class EdObmep2009SchoolSpider(BaseSchoolSpider):
    name = 'obmep2009-school'
    id_edition_url = '2009'
    awards = [
        'Kit de material esportivo e livros/vídeos para a composição de uma biblioteca básica em Matemática e Ciências',
        'Livros/vídeos para a composição de uma biblioteca básica em Matemática e Ciências',
        'Troféu',
    ]
