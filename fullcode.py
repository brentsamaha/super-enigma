
#To start, we imported the packages we will use for the project.
import requests
from requests import get
from bs4 import BeautifulSoup

#We assign the variable html to retrieve the html data from the IMDB page that has the information we want.
html = requests.get('https://www.imdb.com/search/title/?count=100&groups=oscar_best_picture_winners&sort=year%2Cdesc&ref_=nv_ch_osc')

soup = BeautifulSoup(html.text, 'html.parser')

#In the IMDB webpage's html, each movie's information is within a div tab with the class "lister-item-content."
movie_info = soup.find_all('div', class_='lister-item-content')

#We create empty lists to store each subset of information.
genres_list = []
certificates_list = []
names_list = []
years_list = []
runtimes_list = []
directors_list = []
actors_list = []
grosses_list = []
ratings_list = []
votings_list = []

#To parse through each line of HTML between the opening and closing tags of lister-item-content. 
#The loop continues as many times as there are movies on the webpage.

for movie in movie_info:

    genre = movie.find('span', class_='genre').text
    stripped_genre=genre.strip()                           #stripping the text as multiple right spaces were observed 
    genres_list.append([stripped_genre])                   #stripped_genre is in brackets as many movies has multiple genres listed, creating sublists keeps the genres together
   
    certificate = movie.find('span', class_='certificate').text
    certificates_list.append(certificate)
    
    name = movie.h3.a.text
    names_list.append(name)
    
    year = movie.h3.find ("span", class_= "lister-item-year text-muted unbold").text
    year_clean1 = year[-5:-1]                             #indexing the text to remove any parentheses or roman numerals in text 
    years_list.append(year_clean1)
    
    runtime = movie.find('span', class_='runtime').text
    runtimes_list.append(runtime)
    
    director = movie.find('p',class_='').find_all('a')[0].text
    directors_list.append(director)
    
    actors_list.append([a.text for a in movie.find('p',class_='').find_all('a')[1:]])           #bracket allows list of actors per movie to be together in sublist of total actors_list
    
    voting=(movie.find('span', attrs = {'name':'nv'})['data-value'])
    votings_list.append(voting)
    
    nv = movie.find_all('span', attrs = {'name':'nv'})
    gross = nv[1].text if len(nv) > 1 else '-'            #necessary as not every movie has a displayed gross.
    grosses_list.append(gross)
    
    rating=(movie.find('strong')).get_text()
    ratings_list.append(rating)
    
    

#print all information within lists
print('Genres:', genres_list, 'Names:', names_list, 'Certificates:', certificates_list, 'Years:', years_list, 'Runtimes:', runtimes_list, 
      'Directors:', directors_list,'Actors:', actors_list, 'Grosses:', grosses_list, 'Ratings:', ratings_list, 'Votings:', votings_list, sep='\n\n')
