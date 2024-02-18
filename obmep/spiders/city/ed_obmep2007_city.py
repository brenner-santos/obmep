from obmep.spiders.base.city import BaseCitySpider


class EdObmep2007CitySpider(BaseCitySpider):
    name = 'obmep2007-city'
    id_edition_url = '2007'
    report = 'verRelatorioMunicipiosPremiados'
    awards = ['Troféu']
