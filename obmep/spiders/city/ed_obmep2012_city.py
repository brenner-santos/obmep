from obmep.spiders.base.city import BaseCitySpider


class EdObmep2012CitySpider(BaseCitySpider):
    name = 'obmep2012-city'
    id_edition_url = '2012'
    awards = ['Troféu']
