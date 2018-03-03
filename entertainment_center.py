import media
import fresh_tomatoes
import urllib2
import json

key_api = 'fe09bc7261fdf7e9378f67ccbeeb84e1'

# Fetching Gladiator data from API service
glad_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/98?api_key="+key_api)
gladvid_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/98/videos?api_key="+key_api)
glad_data = json.load(glad_obj)
gladvid_data = json.load(gladvid_obj)
for item in gladvid_data["results"]:
    glad_yt_key = item["key"]

# Creating Gladiator object
gladiator = media.Movie(glad_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+glad_data["poster_path"],
	"https://www.youtube.com/watch?v="+glad_yt_key)

# Fetching Godfather data from API service
god_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/238?api_key="+key_api)
godvid_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/238/videos?api_key="+key_api)
god_data = json.load(god_obj)
godvid_data = json.load(godvid_obj)
for item in godvid_data["results"]:
    god_yt_key = item["key"]

# Creating Godfather object
the_godfather = media.Movie(god_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+god_data["poster_path"],
	"https://www.youtube.com/watch?v="+god_yt_key)

# Fetching 12monkeys data from API service
tw_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/63?api_key="+key_api)
twvid_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/63/videos?api_key="+key_api)
tw_data = json.load(tw_obj)
twvid_data = json.load(twvid_obj)
for item in twvid_data["results"]:
    tw_yt_key = item["key"]

# Creating 12monkeys object
twelve_monkeys = media.Movie(tw_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+tw_data["poster_path"],
	"https://www.youtube.com/watch?v="+tw_yt_key)

# Fetching Cuckoo data from API service
cuck_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/510?api_key="+key_api)
cuckvid_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/510/videos?api_key="+key_api)
cuck_data = json.load(cuck_obj)
cuckvid_data = json.load(cuckvid_obj)
for item in cuckvid_data["results"]:
    cuck_yt_key = item["key"]

# Creating Cuckoo object
cuckoo_nest = media.Movie(cuck_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+cuck_data["poster_path"],
	"https://www.youtube.com/watch?v="+cuck_yt_key)

# Fetching Matrix data from API service
mat_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/603?api_key="+key_api)
matvid_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/603/videos?api_key="+key_api)
mat_data = json.load(mat_obj)
matvid_data = json.load(matvid_obj)
for item in matvid_data["results"]:
    mat_yt_key = item["key"]

# Creating Matrix object
the_matrix = media.Movie(mat_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+mat_data["poster_path"],
	"https://www.youtube.com/watch?v="+mat_yt_key)

# Fetching American Beauty data from API service
ame_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/14?api_key="+key_api)
amevid_obj = urllib2.urlopen("https://api.themoviedb.org/3/movie/14/videos?api_key="+key_api)
ame_data = json.load(ame_obj)
amevid_data = json.load(amevid_obj)
for item in amevid_data["results"]:
    ame_yt_key = item["key"]

# Creating American Beauty object
american_beauty = media.Movie(ame_data["title"],
	"https://image.tmdb.org/t/p/w600_and_h900_bestv2/"+ame_data["poster_path"],
	"https://www.youtube.com/watch?v="+ame_yt_key)

movies = [the_godfather, twelve_monkeys, the_matrix, american_beauty, gladiator, cuckoo_nest]
fresh_tomatoes.open_movies_page(movies)
