from obmep.spiders.base.school import BaseSchoolSpider


class EdObmep2006SchoolSpider(BaseSchoolSpider):
    name = 'obmep2006-school'
    id_edition_url = '2006'
    awards = [
        'Notebook c/ kit de projeção móvel (datashow) e livros para a composição de uma biblioteca básica em Matemática',
        'Livros para a composição de uma biblioteca básica em Matemática',
    ]
