import json
from ..items import JobseekerIdItem

import scrapy


class jobseekerId(scrapy.Spider):
    name = "jobseeker_id"

    def start_requests(self):
        # Load URLs from the JSON file
        with open('./jobseeker_id/data/job_link/urls.json', 'r') as file:
            data = json.load(file)
        
        dynamic_urls = data.get('job_link', [])

        for url in dynamic_urls:
            yield scrapy.Request(url=url, callback=self.parse_job_info)

    def parse_job_info(self, response):
        items = JobseekerIdItem()

        job_name = response.css('.m-0::text').extract_first()
        job_requirement = response.css('.mb-3 li::text').extract()
        job_desc = response.css('.jbs-content.mb-4 li::text').extract()

        items['job_name'] = job_name
        items['job_requirement'] = job_requirement
        items['job_desc'] = job_desc

        yield {
                'job_name' : job_name,
                'job_requirement' : job_requirement,
                'job_desc' : job_desc
        }