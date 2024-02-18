from obmep.spiders.base.city import BaseCitySpider


class EdObmep2005CitySpider(BaseCitySpider):
    name = 'obmep2005-city'
    id_edition_url = '2005'
    report = 'verRelatorioMunicipiosPremiados'
    awards = ['Quadras de Esporte', 'Certificado de Mérito Nacional']
