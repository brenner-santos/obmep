from obmep.spiders.base.city import BaseCitySpider


class EdObmep2011CitySpider(BaseCitySpider):
    name = 'obmep2011-city'
    id_edition_url = '2011'
    awards = ['Troféu']
