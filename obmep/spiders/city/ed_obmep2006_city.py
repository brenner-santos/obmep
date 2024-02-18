from obmep.spiders.base.city import BaseCitySpider


class EdObmep2006CitySpider(BaseCitySpider):
    name = 'obmep2006-city'
    id_edition_url = '2006'
    report = 'verRelatorioMunicipiosPremiados'
    awards = ['Quadras de Esporte', 'Troféu']
