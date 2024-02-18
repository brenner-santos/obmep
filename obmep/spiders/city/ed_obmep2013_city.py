from obmep.spiders.base.city import BaseCitySpider


class EdObmep2013CitySpider(BaseCitySpider):
    name = 'obmep2013-city'
    id_edition_url = '2013'
    awards = ['Troféu']
