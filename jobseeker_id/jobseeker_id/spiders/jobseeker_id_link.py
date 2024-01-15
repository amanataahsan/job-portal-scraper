from ..items import JobseekerIdItem
from ..conf import conf
import scrapy

class jobseekerIdLink(scrapy.Spider):
    name = 'jobseeker_id_link'

    start_urls = [
        f"https://jobseeker.id/jobs/vacancy?keyword={conf.keyword}&specialization={conf.spec}&address={conf.city}&sort={conf.sort_type}&limit={conf.limit}",
    ]

    def parse_job_info(self, response):
        items = JobseekerIdItem()

        job_name = response.css('.m-0::text').extract_first()
        job_requirement = response.css('.mb-3 li::text').extract()
        job_desc = response.css('.jbs-content.mb-4 li::text').extract()
    
        if len(job_requirement):
            pass
        else:
            job_requirement = response.css('.mb-3 p::text').extract()
        
        if len(job_desc):
            pass
        else:
            job_desc = response.css('.jbs-content.mb-4 p::text').extract()

        items['job_name'] = job_name
        items['job_requirement'] = job_requirement
        items['job_desc'] = job_desc

        yield {
                'job_name' : job_name,
                'job_requirement' : job_requirement,
                'job_desc' : job_desc
        }

    def parse(self, response):
        for i in range(conf.limit):
            a = i+1
            xpath = f'//*[@id="main-wrapper"]/section/div/div/div/div[2]/div[{a}]/div/div[1]/div[2]/a/@href'
            yield response.follow(str(response.xpath(xpath).get()), callback=self.parse_job_info)
        
        next_page = response.css('.pagination .active~ li+ li a::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


#HW : multiple keyword