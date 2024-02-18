from obmep.spiders.base.city import BaseCitySpider


class EdObmep2008CitySpider(BaseCitySpider):
    name = 'obmep2008-city'
    id_edition_url = '2008'
    awards = ['Troféu']
