from scrapy.crawler import CrawlerProcess

from ResidentCrawler.ResidentCrawler.spiders.resident_spider import ResidentSpider


def main(event, context):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': '/tmp/overall_events.csv'
    })

    process.crawl(ResidentSpider)
    process.start()
    print('All done.')


if __name__ == "__main__":
    main('', '')