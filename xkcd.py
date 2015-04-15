#Downloads all the available xkcd comics from their archives
#Thanks to the creator for making these free to copy and share these beautiful comics
from bs4 import BeautifulSoup
import urllib2
import re


#proxy authentication
def getproxy() :
	proxy = urllib2.ProxyHandler({'http': 'http://s.sayak:kx8qnSBY@202.141.80.19:3128'})
	auth = urllib2.HTTPBasicAuthHandler()
	opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	urllib2.install_opener(opener)




#some bookkeeping at the start
def download():

	baseurl = 'http://xkcd.com'
	html = urllib2.urlopen('http://xkcd.com/archive').read()
	#make soup 
	soup = BeautifulSoup(html,"lxml")

	#find the most recent publication
	maxVal = soup.find(id ="middleContainer").find_all('a')[0]['href']
	#extracting number in between slashes
	#could have used .split() which would have been better, buti wanted to see how regexes work
	maxVal = re.search('/(.+?)/', maxVal).group(1)
	

	#int(maxVal)+1

	for i in range(1,100):
		print "Comic no "+str(i)
		url =baseurl+'/'+str(i)+'/'
		#print url
		getPage(url,i)
		

	print("All done!")	





def getPage(url,index):
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html,"lxml")

	#extract image link and name
	imgLink = 'http:'+ soup.find(id ="comic").find('img').get('src')
	name = soup.find(id ="ctitle").string
	
	#makink sure that the extension of dnld file jpg/png is taken into acc when saving the file
	extension = imgLink.split('.')[-1]


	img = open("./images/"+name+"_"+str(index)+ "."+extension,'wb')
	img.write(urllib2.urlopen(imgLink).read())
	img.close()

	



def main() :
	try:
		html = urllib2.urlopen('http://xkcd.com/').getcode()
	except Exception, e:
		if e.code == 200:
			pass
		elif e.code == 407:
		   getproxy()
		   download()
		else:
			print("Webpage cannot be contacted, exiting program");   	



if __name__ == '__main__':
	main()

