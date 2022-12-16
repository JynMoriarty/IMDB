import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from .. items import ImdbItem


class ImdbSpider(CrawlSpider):
    name = 'imdb_spider'
    allowed_domains = ['imdb.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'imdb.pipelines.MovieScrapingPipeline': 300
        }
        }

    rules = (
        Rule(LinkExtractor(restrict_css = 'td.titleColumn > a'), callback='parse_item', follow=False),
    )
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers={
            'User-Agent': self.user_agent
        })

    def parse_item(self, response):
        
        durée = response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/text()").extract()
        items = ImdbItem()
        
        items['title'] = response.xpath("//h1/text()").get()
        items['date']= response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/a/text()").get()
        items['score']= response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()").get()
        items['genre']= response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/div[2]/a/span/text()").get()
        if len(durée) == 5:
            items['duree']= int(durée[0])*60 + int(durée[3])
        else :
            items['duree'] = int(durée[0])
        items['description'] = response.xpath('//span[@class="sc-16ede01-1 kgphFu"]/text()').get()
        items['acteurs'] = response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li/a/text()").extract()
        items['public'] = response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]/a/text()").get()
        items['origine'] = response.xpath("/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[@class='ipc-page-section ipc-page-section--base celwidget']/div[@class='sc-f65f65be-0 ktSkVi']/ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base']/li[@class='ipc-metadata-list__item'][1]/div[@class='ipc-metadata-list-item__content-container']/ul[@class='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base']/li[@class='ipc-inline-list__item']/a[@class='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']/text()").extract()
        items['url']= response.url
        items['image']= response.xpath("//img[@class='ipc-image']/@src").extract()[0]
        yield items 
    
class ImdbsSpider(CrawlSpider):
    name = 'imdbs_spider'
    allowed_domains = ['imdb.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'imdb.pipelines.SerieScrapingPipeline': 300
        }
        }
    rules = (
        Rule(LinkExtractor(restrict_css = 'td.titleColumn > a'), callback='parse_item', follow=False),
        
    )
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250', headers={
            'User-Agent': self.user_agent
        })
    
    def parse_item(self, response):
        items = ImdbItem()

        durée = response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[4]/text()").extract()
            
        items['title'] = response.xpath("//h1/text()").get()
        items['date'] = response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]/a/text()").get()
        items['score']= response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()").get()
        items['genre']= response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/div[2]/a/span/text()").get()
        
        if durée == []:
            items['duree'] = 'ya r frero'
        elif len(durée) == 5:
            items['duree']= int(durée[0])*60 + int(durée[3])
        else :
            items['duree'] = int(durée[0])
        items['description'] = response.xpath('//span[@class="sc-16ede01-1 kgphFu"]/text()').get()
        items['acteurs'] =  response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li/div/ul/li/a/text()").extract()
        items['public'] = response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/a/text()").get()
        items['origine'] = response.xpath("/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[@class='ipc-page-section ipc-page-section--base celwidget']/div[@class='sc-f65f65be-0 ktSkVi']/ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base']/li[@class='ipc-metadata-list__item'][1]/div[@class='ipc-metadata-list-item__content-container']/ul[@class='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base']/li[@class='ipc-inline-list__item']/a[@class='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']/text()").extract()
        yield items



