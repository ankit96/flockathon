import urllib2

import os
from bs4 import BeautifulSoup
def mirchi():
	response = urllib2.urlopen('http://www.radiomirchi.com/more/mirchi-top-20/')
	htmlsrc = response.read()
	
	htmlsrc = htmlsrc.split('<article', 1)[1]
	articles = htmlsrc.split('</article>')

	songs=[]
	for article in articles:
		try:
			songs.append((article.split('<h2>')[1].split('</h2>', 1)[0], article.split('<h3>')[1].split('<br>', 1)[0]))
		except:
			pass

	return songs


def gaana():
	response = urllib2.urlopen('https://www.kkbox.com/my/en/charts/international-daily-song-latest.html')
	htmlsrc = response.read()
	soup = BeautifulSoup(htmlsrc)
	songs=""
    	soup1 = soup.findAll('h4')
	soup2 = soup.findAll('span', {"class": "non-link-type"})
	
	#soup = soup.findAll('h4')
	i=0
	try:
		for a in soup1[:20]:
			if len(songs)<2:
				songs = a.text + " " +soup2[i].text
			else:
				songs = songs+","+a.text + " " +soup2[i].text
			i=i+1
			
		return  songs
	except:
		print songs
	#print soup[0].text
	


#gaana("30")
'''

data =  mirchi()
for a in data:
	print a[0] + " " + a[1]
	

'''
