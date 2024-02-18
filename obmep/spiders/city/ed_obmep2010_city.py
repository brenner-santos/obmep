from obmep.spiders.base.city import BaseCitySpider


class EdObmep2010CitySpider(BaseCitySpider):
    name = 'obmep2010-city'
    id_edition_url = '2010'
    awards = ['Troféu']
