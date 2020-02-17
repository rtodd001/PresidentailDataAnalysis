import scrapy

class SurveyUSA1TablesSpider(scrapy.Spider):
	name = "surveyusa1"

	def start_requests(self):
		urls = ['http://www.surveyusa.com/client/PollReport_main.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759',]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for row in response.xpath('//*[@class="qtable"]//tr'):
			yield {
				'r1' : row.xpath('td[1]//text()').extract_first(),
				'r2' : row.xpath('td[2]//text()').extract_first(),
				'r3' : row.xpath('td[3]//text()').extract_first(),
				'r4' : row.xpath('td[4]//text()').extract_first(),
				'r5' : row.xpath('td[5]//text()').extract_first(),
				'r6' : row.xpath('td[6]//text()').extract_first(),
				'r7' : row.xpath('td[7]//text()').extract_first(),
				'r8' : row.xpath('td[8]//text()').extract_first(),
				'r9' : row.xpath('td[9]//text()').extract_first(),
				'r10' : row.xpath('td[10]//text()').extract_first(),
				'r11' : row.xpath('td[11]//text()').extract_first(),
			}
