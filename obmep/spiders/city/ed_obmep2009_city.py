from obmep.spiders.base.city import BaseCitySpider


class EdObmep2009CitySpider(BaseCitySpider):
    name = 'obmep2009-city'
    id_edition_url = '2009'
    awards = ['Troféu']
