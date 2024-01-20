import scrapy


class City(scrapy.Item):
    state_code = scrapy.Field()
    city = scrapy.Field()


class School(scrapy.Item):
    state_code = scrapy.Field()
    city = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()


class Student(scrapy.Item):
    level = scrapy.Field()
    name = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()
    city = scrapy.Field()
    state_code = scrapy.Field()
    medal = scrapy.Field()
    honorable_mention = scrapy.Field()


class Teacher(scrapy.Item):
    state_code = scrapy.Field()
    city = scrapy.Field()
    teacher = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()
    group = scrapy.Field()
