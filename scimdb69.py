from imdb import IMDb

#['airing', 'akas', 'alternate versions', 'awards', 'connections', 'crazy credits', 'critic reviews', 'episodes', 'external reviews', 'external sites', 'faqs', 'full credits', 'goofs', 'keywords', 'locations', 'main', 'misc sites', 'news', 'official sites', 'parents guide', 'photo sites', 'plot', 'quotes', 'release dates', 'release info', 'reviews', 'sound clips', 'soundtrack', 'synopsis', 'taglines', 'technical', 'trivia', 'tv schedule', 'video clips', 'vote details']


# create an instance of the IMDb class
ia = IMDb()
fich=open("moviestitles.txt","w")

a,b,c,d,e,f,g=0,0,0,0,0,0,0

while(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))!='7131622': 
	movie = ia.get_movie(str(a)+str(b)+str(c)str(d)+str(e)+str(f)+str(g))
	#print('title')
	fichier.write(str(a)+str(b)+str(c)str(d)+str(e)+str(f)+str(g))
	fichier.write("/")
	fich.write(movie.get('title'))
	fichier.write("/")
	fichier.write(movie.get('Votes')
	if g==9:
		g=0
		f+=1
	else:
		g+=1
	if f==9:
		f=0
		e+=1
	if e==9:
		e=0
		d+=1
	if d==9:
		d=0
		c+=1
	if c==9:
		c=0
		b+=1
	if b==9:
		b=0
		a+=1
	print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))
	


#print('/nplo/n')
#print(movie.get('plot'))
#print('/synopsys/n')
#print(movie.get('synopsis'))

# print the names of the directors of the movie
#print('Directors:')
#for director in movie['directors']:
#    print(director['name'])

# print the genres of the movie
#print('Genres:')
#for genre in movie['genres']:
#    print(genre)


#print(ia.get_movie_infoset())

# search for a person name
#people = ia.search_person('Mel Gibson')
#for person in people:
#   print(person.personID, person['name'])


