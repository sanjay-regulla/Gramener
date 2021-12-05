from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import  render
#import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.

class IMDBRating(View):

	def get(self,request):
		

		imdb_top_250_url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

		#myURL = urlopen(imdb_top_250_url)
		r = urlopen(imdb_top_250_url).read()
		soup = BeautifulSoup(r,"html.parser")
		#print(myURL.read())
		top_250_object = soup.find_all("tr")
		top_250_movies_list = []
		for row in top_250_object:
			
			if row.find_all('td') :
				movie_name = row.find_all('a')[1].text.encode('utf-8').decode("utf-8") 
				
				text = row.find_all('strong')[0].get('title', 'No title attribute')
				text = text.replace(' based on ','-',).replace(' user ratings','').split('-')
				rating = float(text[0])
				users = float(text[1].replace(',',''))
				top_250_movies_list.append([str(movie_name),rating,users])
		return render(request,'scatter_plot.html',locals())