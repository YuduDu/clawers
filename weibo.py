#-*-coding:utf8-*-

import urllib
from bs4 import BeautifulSoup
import cookielib
import glob
import os
import urllib2, cookielib
import urlparse
import sys

reload(sys) 
sys.setdefaultencoding('utf-8')

path = 'PATHTO/IFTTT/Weibo'

def get_pics(page):
	parsed = BeautifulSoup(page.read())
	pics = parsed.body.find_all('div')
	for pic in pics:
		try:
			imglink = pic.find('a',text='原图')
			imglink = 'http://weibo.cn/'+imglink['href']
			print "imglink "+imglink
			image = openurl(imglink)
			splitPath = imglink.split('/')
			fName = splitPath.pop()
			f = open(path+'/'+fName+'.jpg', 'wb')
			f.write(image.read())
			f.close()
		except:
			pass


def openurl(url):
	header = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'}
	cj = cookielib.MozillaCookieJar('YOURCOOKIES.txt')
	cj.load()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)
	req = urllib2.Request(url, None, header)
	handle = urllib2.urlopen(req)
	return handle

for htmlfile in glob.glob(os.path.join(path,'*.html')):
	print "htmlfile: "+htmlfile;
	html = open(htmlfile)
	content = html.read()
	parsed_html = BeautifulSoup(content)
	url = parsed_html.body.find("a").text
	o = urlparse.urlparse(url)
	param_dict = urlparse.parse_qs(o.query)
	try:
		url = param_dict['url'][0][17:]
	except:
		continue
 	url = 'http://weibo.cn/'+url
 	print url

	handle = openurl(url)
	#print handle.read()
	page = BeautifulSoup(handle.read())
	part = page.body.find('div',attrs={'id':'M_'})
	addrs = part.div.find_all('a')
	pics_mode =0
	result1 = False
	result2 = False
	for addr in addrs:
		print addr.text
		if "组图" in addr.text:
			pics_mode =1
			pics_addr = 'http://weibo.cn/'+addr['href']
			print '组图' + pics_addr
			handle = openurl(pics_addr)
			get_pics(handle)
			result1=True
		else:
			continue
	if pics_mode == 0:
		pics = part.find_all('a',text='原图')
		if pics != []:
			for pic in pics:
				imglink = 'http://weibo.cn/'+pic['href']
				print "单图 "+imglink
				image = openurl(imglink)
				splitPath = imglink.split('/')
				fName = splitPath.pop()
				f = open(path+'/'+fName+'.jpg', 'wb')
				f.write(image.read())
				f.close()
			result2 = True
		else:
			result2 = False
		
	# try video:
	#print result1
	#print result2
	#if result1 == result2:
	#	for addr in addrs:
	#		if 'http' in addr.text:
	#			print addr.text
	#			page = openurl(addr.text)
	#			print page.read()

	if result1 or result2:
		os.system('rm '+str(htmlfile))



