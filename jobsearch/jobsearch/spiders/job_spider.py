import scrapy
from jobsearch.items import JobsearchItem
import json

class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["domain"]
    start_urls = [
    ]# "websitesurl"

    def start_requests(self):
        headers =  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'websitesurl'
        }
        #data = api-param 
        yield scrapy.Request("api header /?data="+data,headers=headers, callback=self.parse_job)
        

    def parse_job(self, response):  
        #item = JobsearchItem() 
        print(list(self.find('PositionTitle', response.text)))
        with open('filename', 'w',encoding='utf8') as f:
            f.write(response.text)
        #item['JOB_NAME'] = 
        
