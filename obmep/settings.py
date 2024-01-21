BOT_NAME = 'obmep'
SPIDER_MODULES = ['obmep.spiders']
NEWSPIDER_MODULE = 'obmep.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'obmep.pipelines.DefaultValuesPipeline': 200,
    'obmep.pipelines.SQLDatabasePipeline': 500,
}

OBMEP_DATABASE_URL = 'sqlite:///obmep.db'

LOG_LEVEL = 'WARNING'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
