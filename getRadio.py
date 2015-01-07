# Written by Michael Hawley, 2015

import sched, time
import datetime
import re
import urllib
from urllib import request

s = sched.scheduler(time.time, time.sleep)

def getTime():
	# prints the current time in the console
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print(st)

request_interval = 30 # seconds

url = "http://www.bandconditions.com/" # site to be scrubbed
html_re = re.compile('\d*.jpg') # digits with suffix ".jpg"
value = re.compile('\d*') # digits

def findBandConditions(content):
	# scrapes the content of a website for the html_re regular expression
	names = html_re.findall(content)
	values = []
	for i in range(len(names)):
		digits = (value.search(names[i]).group())
		values.append(digits)
	print(values)
	return(values)
	

def getResponse(sc):
	# opens and decodes the content of a URL as text once per request interval
	response = urllib.request.urlopen(url)
	webContent = response.read().decode('utf-8')
	findBandConditions(webContent)
	sc.enter(request_interval, 1, getResponse, (s,))
	getTime()

s.enter(0, 1, getResponse, (s,))
s.run()
