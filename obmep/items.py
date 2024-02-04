from scrapy.item import Field, Item


class CityItem(Item):
    created_at = Field()
    edition = Field()
    award = Field()
    name = Field()
    state_code = Field()


class SchoolItem(Item):
    created_at = Field()
    edition = Field()
    award = Field()
    name = Field()
    type = Field()
    group = Field()
    city_name = Field()
    state_code = Field()


class StudentItem(Item):
    created_at = Field()
    edition = Field()
    award = Field()
    name = Field()
    level = Field()
    school = Field()


class TeacherItem(Item):
    created_at = Field()
    edition = Field()
    award = Field()
    name = Field()
    group = Field()
    schools = Field()
