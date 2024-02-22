import click
from scrapy.crawler import CrawlerProcess
from scrapy.spiderloader import SpiderLoader
from scrapy.utils.project import get_project_settings

from obmep.__version__ import __version__


def get_all_spiders():
    settings = get_project_settings()
    spider_loader = SpiderLoader.from_settings(settings)
    return spider_loader.list()


all_spiders = get_all_spiders()
all_editions = set(spider.split('-', 1)[0] for spider in all_spiders)
all_tables = set(spider.split('-', 1)[1] for spider in all_spiders)


@click.group()
@click.version_option(__version__)
def main():
    pass


@main.command()
def editions():
    """List editions"""
    for edition in sorted(all_editions):
        click.echo(edition)


@main.command()
def tables():
    """List tables"""
    for edition in sorted(all_tables):
        click.echo(edition)


def crawl_spiders(spiders: list[str]):
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    for spider in spiders:
        process.crawl(spider)
    process.start()


def crawl_all_spiders(ctx, param, value):
    if value:
        crawl_spiders(all_spiders)
        ctx.exit()


@main.command()
@click.option(
    '-e',
    '--edition',
    metavar='EDITION',
    type=click.Choice(all_editions),
    default=None,
    help='Crawl a edition',
)
@click.option(
    '-t',
    '--table',
    metavar='TABLE',
    type=click.Choice(all_tables),
    default=None,
    help='Crawl a table',
)
@click.option(
    '-a',
    '--all',
    type=click.BOOL,
    default=False,
    is_eager=True,
    is_flag=True,
    callback=crawl_all_spiders,
    help='Crawl all tables of all editions',
)
@click.pass_context
def crawl(ctx, edition=None, table=None, all=False):
    """Run spiders"""
    if not edition and not table:
        click.echo(ctx.get_help())
        ctx.exit()

    if edition:
        spiders = [
            spider for spider in spiders if edition == spider.split('-', 1)[0]
        ]
    if table:
        spiders = [
            spider for spider in spiders if table == spider.split('-', 1)[1]
        ]
    crawl_spiders(spiders)
