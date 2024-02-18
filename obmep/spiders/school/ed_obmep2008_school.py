from obmep.items import SchoolItem
from obmep.spiders.base.school import BaseSchoolSpider


class EdObmep2008SchoolSpider(BaseSchoolSpider):
    name = 'obmep2008-school'
    id_edition_url = '2008'
    awards = [
        'Kit para exibição audiovisual e livros para a composição de uma biblioteca básica em Matemática e Ciências',
        'Troféu',
        'Livros para a composição de uma biblioteca básica em Matemática e Ciências',
    ]
