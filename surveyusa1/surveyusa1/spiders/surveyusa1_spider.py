import scrapy

class SurveyUSASpider(scrapy.Spider):
	name = 'data'

	def start_requests(self):
		urls = ['http://www.surveyusa.com/client/PollReport_main.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759', ]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'data-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)
