import scrapy


class CityItem(scrapy.Item):
    edition = scrapy.Field()
    state_code = scrapy.Field()
    city = scrapy.Field()


class SchoolItem(scrapy.Item):
    edition = scrapy.Field()
    state_code = scrapy.Field()
    city = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()
    group = scrapy.Field()


class StudentItem(scrapy.Item):
    edition = scrapy.Field()
    level = scrapy.Field()
    name = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()
    city = scrapy.Field()
    state_code = scrapy.Field()
    medal = scrapy.Field()
    honorable_mention = scrapy.Field()


class TeacherItem(scrapy.Item):
    edition = scrapy.Field()
    state_code = scrapy.Field()
    city = scrapy.Field()
    teacher = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()
    group = scrapy.Field()
