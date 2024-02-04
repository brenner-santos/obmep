import datetime as dt
import json
import os


class DefaultValuesPipeline:
    def open_spider(self, spider):
        self.created_at = dt.datetime.utcnow()

    def process_item(self, item, spider):
        item['edition'] = getattr(spider, 'name').split('-')[0]
        item['created_at'] = self.created_at

        for field, value in item.items():
            if isinstance(value, (str, list, dict)):
                item[field] = self.clear_field(value)

        return item

    def clear_field(self, value):
        if isinstance(value, str):
            return value.strip()
        elif isinstance(value, list):
            return [self.clear_field(elem) for elem in value]
        elif isinstance(value, dict):
            return {key: self.clear_field(val) for key, val in value.items()}
        return value


class JsonPipeline:
    def open_spider(self, spider):
        edition_code, table = getattr(self, 'name').split('-', 1)
        filename = f'./data/{table}/{edition_code}.json'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.file = open(filename, 'w')
        self.data = []

    def close_spider(self, spider):
        self.file.write(json.dumps(self.data, default=str, indent=1))
        self.file.close()

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item
