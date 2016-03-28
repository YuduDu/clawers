import urllib
from BeautifulSoup import BeautifulSoup
import cookielib
import glob
import os
import json

path = "YOUR_PATH_TO_IFTTT_TWITTER"
result1 = False
result2 = False

def getmedia(addr):
	u = urllib.urlopen(addr)
	data =u.read()
	splitPath = addr.split('/')
	fName = splitPath.pop()
	f = open(path+'/'+fName, 'wb')
	f.write(data)
	f.close()
	return True


for htmlfile in glob.glob(os.path.join(path,'*.html')):
	html = open(htmlfile)
	content = html.read()
	parsed_html_1=BeautifulSoup(content)
	url = parsed_html_1.body.find('a',attrs={'style':'color: #33ccff;'}).text
	resource = urllib.urlopen(url)
	#print resource.read()
	parsed_html = BeautifulSoup(resource)
	try:
		divs = parsed_html.body.findAll('div', attrs={'class':'AdaptiveMedia-photoContainer js-adaptive-photo '})
	except:
		divs = None
	if divs is not None:
		for div in parsed_html.body.findAll('div', attrs={'class':'AdaptiveMedia-photoContainer js-adaptive-photo '}):
			result1 = getmedia(div.find('img')['src'])
	
	try:
		video = parsed_html.head.find('meta',attrs={'property':'og:video:url'})
	except:
		video =None
	if video is not None:
		page = urllib.urlopen(video['content'])
		parsed_page = BeautifulSoup(page)
		try:
			div = parsed_page.body.find('div',attrs={'id':'playerContainer'})
		except:
			div = None
		if div is not None:
			data = div['data-config']
			video_addr = json.loads(data)['video_url']
			result2 = getmedia(video_addr)

	if result1 or result2:
		os.system('rm '+str(htmlfile))

