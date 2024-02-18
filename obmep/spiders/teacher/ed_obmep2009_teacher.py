from obmep.spiders.base.teacher import BaseTeacherSpider


class EdObmep2009TeacherSpider(BaseTeacherSpider):
    name = 'obmep2009-teacher'
    id_edition_url = '2009'
    awards = [
        'Placa de Homenagem e Coleção de livros escolhida pela Direção Acadêmica da OBMEP'
    ]
