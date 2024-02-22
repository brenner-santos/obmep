import click
from scrapy.crawler import CrawlerProcess
from scrapy.spiderloader import SpiderLoader
from scrapy.utils.project import get_project_settings

from obmep.__version__ import __version__


def get_all_spiders():
    spider_loader = SpiderLoader.from_settings(get_project_settings())
    return spider_loader.list()


def get_editions(spiders: list[str] = get_all_spiders()):
    return set(spider.split('-', 1)[0] for spider in spiders)


def get_tables(spiders: list[str] = get_all_spiders()):
    return set(spider.split('-', 1)[1] for spider in spiders)


@click.group()
@click.version_option(__version__)
def main():
    pass


@main.command()
def editions():
    """List editions"""
    for edition in sorted(get_editions()):
        click.echo(edition)


@main.command()
def tables():
    """List tables"""
    spiders = get_all_spiders()
    for table in sorted(get_tables()):
        click.echo(table)


def crawl_spiders(spiders: list[str]):
    process = CrawlerProcess(get_project_settings())
    for spider in spiders:
        process.crawl(spider)
    process.start()


def crawl_all_spiders(ctx, param, value):
    if value:
        crawl_spiders(get_all_spiders())
        ctx.exit()


@main.command()
@click.option(
    '-e',
    '--edition',
    metavar='EDITION',
    type=click.Choice(get_editions()),
    default=None,
    help='Crawl a edition',
)
@click.option(
    '-t',
    '--table',
    metavar='TABLE',
    type=click.Choice(get_tables()),
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

    spiders = get_all_spiders()
    if edition:
        spiders = [
            spider for spider in spiders if edition == spider.split('-', 1)[0]
        ]
    if table:
        spiders = [
            spider for spider in spiders if table == spider.split('-', 1)[1]
        ]
    crawl_spiders(spiders)
