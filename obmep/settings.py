BOT_NAME = 'obmep'
SPIDER_MODULES = ['obmep.spiders']
NEWSPIDER_MODULE = 'obmep.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'obmep.pipelines.DefaultValuesPipeline': 100,
    'obmep.pipelines.JsonPipeline': 200,
}

OBMEP_DATABASE_URL = 'sqlite:///obmep.db'

LOG_LEVEL = 'WARNING'

EXTENSIONS = {
    'obmep.extensions.StatsPersist': 500,
}

HTTPCACHE_ENABLED = True
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
DOWNLOAD_DELAY = 2

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
