from ..items import JobseekerIdItem
from ..conf import conf
import scrapy
from .. import helper

class jobseekerIdLink(scrapy.Spider):
    name = 'seek_au'
    start_urls = [
        # "https://www.seek.com.au/job/73575459?ref=search-standalone&type=standard#sol=7ca463c0c899259eb103101da8ec575b01cde049"
        # "https://www.seek.com.au/job/73649903?ref=search-standalone&type=standout#sol=b69d69176cc952f66e36a9097935960f31c43ada"
        # "https://www.seek.com.au/job/73522803?ref=search-standalone&type=standout#sol=aa05de8f392d95deb148217621220a0e12af6dd0"
        "https://www.seek.com.au"
        # 'https://www.seek.com.au/job/73575459?ref=search-standalone&type=standard#sol=7ca463c0c899259eb103101da8ec575b01cde049'
    ]
    # start_urls = [
    #     'https://www.seek.com.au/job/73521093?type=standard&ref=search-standalone#sol=b16c8fbb4ae4b6465b3890fa7a80e4d819379204',
    #     'https://www.seek.com.au/job/73515043?type=standout&ref=search-standalone#sol=9febc3dcc3fc635e32b17f8281260677671600da',
    #     'https://www.seek.com.au/job/73517839?type=standard&ref=search-standalone#sol=5f877ee58f4af84e5d082b9967c4be24f543c5db',
    #     'https://www.seek.com.au/job/73525003?type=standard&ref=search-standalone#sol=b18ba57d9f4da6de294bc5d96b87da6b96b9504e',
    #     'https://www.seek.com.au/job/73516273?type=standout&ref=search-standalone#sol=65861ec3702776c59b31f9c1bcfcc96f8ba85e27',
    #     'https://www.seek.com.au/job/73582477?ref=search-standalone&type=promoted#sol=218baf3c99c6498509f8eafd5a2fbacce9dca033'
    # ]

    # def start_url(self, keyword: str, spec: str, city: str, sort_type: str, limit: int):
    #     return f"https://jobseeker.id/jobs/vacancy?keyword={keyword}&specialization={spec}&address={city}&sort={sort_type}&limit={limit}"

    # def start_requests(self):
    #     dynamic_urls = [self.start_url(i, conf.spec, conf.city, conf.sort_type, conf.limit) for i in conf.keyword]

    #     for url in dynamic_urls:
    #         print(">>>>>>>>>>>>>>>>>>>>>>>{}".format(url))
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse_job(self, response):
        job_url = response.xpath(f"//a[@data-automation='jobTitle']/@href").extract()

        # yield {
        #     "url": response.xpath(f"//a[@aria-label='Next' or @title='Next']/@href").extract()
        #     , "total_job": len(job_url)
        # }
        
        if job_url:
            for url in job_url:
                yield response.follow(url = url, callback = self.parse_job_skill)
        
        next_page = response.xpath(f"//a[@aria-label='Next' or @title='Next']/@href").get()

        if next_page:
            yield response.follow(url = next_page, callback = self.parse_job)


    def parse_job_skill(self, response):
        items = JobseekerIdItem()
        skills = []

        for skill in conf.contain_skill:
            #with button (ul/li)
            template_1 = response.xpath(f'//strong[contains(translate(text(), "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "{skill}")]/following::ul[1]/li/text()').extract()
            #with "- " in free text
            template_2 = response.xpath(f'//strong[contains(translate(text(), "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "{skill}")]/following::p[starts-with(normalize-space(text()), "- ")]/text()').extract()

            if template_1:
                skills.append(template_1)
            elif template_2:
                skills.append(template_2)
            else :
                skills.append('')
        
        items['job_title'] = response.css('h1[data-automation="job-detail-title"]::text').extract()
        items['job_requirement'] = skills
        items['job_data'] = response.css('div[data-automation="jobAdDetails"]').extract()
        items['job_link'] = response.request.url

        yield items


    def parse(self, response):
        classification_list = response.xpath(f'//*[@id="classificationsPanel"]/nav/ul/li/a/@aria-label').extract()
        # print(classification_list)

        if classification_list:
            result = [
                f"https://www.seek.com.au/jobs-in-{helper.parse_classification(classification)}"
                for classification in classification_list
            ]
        else:
            result = conf.category
        
        for url in result:
            print(">>>>>>>>>>>>>>>>>>>>>>>{}".format(url))
            yield response.follow(url, callback=self.parse_job)