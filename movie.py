import re
import urllib
import urllib2
import json, ast
import cgi
import yaml


class Movie:
    def __init__(self,title = '',
        trailer_youtube_url = '', 
        imdbID ='',omdb_data=''):

        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.imdbID = imdbID
        self.omdb_data = omdb_data
    	self.youtube_id()

    def nice_yaml(self):
        return {'title': self.title, 
        'trailer_youtube_url': self.trailer_youtube_url,
        'imdbID': self.imdbID,
        'omdb_data': ast.literal_eval(json.dumps(self.omdb_data)) }

    def content_to_html(self):
        return ('''
        <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{self.trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
            <img src="{self.omdb_data[Poster]}" width="220" height="342">
            <h2>{self.title}</h2>
        </div>
        ''').format(self = self)

    def youtube_id(self):
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        self.trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
    
    def get_omdb_data(self):
        if self.imdbID:
            search_url = "http://www.omdbapi.com/?i=" + self.imdbID 
            response = urllib2.urlopen(search_url)
            self.omdb_data = json.loads(response.read())
        else:
            print "no imdbID present"

    @classmethod
    def search_omdb_by_title(self, title):
        #put a generator here

        search_url = "http://www.omdbapi.com/?s=" + urllib.quote(title)
        response = urllib2.urlopen(search_url)
        return json.loads(response.read())['Search']



#Takes an input


#makes a class, adds it to file

#writes it to a hash

#has a search option to ... edit the movie

#puts movie into a hash in another file as YAML!
#YAML DB!

#create_movie


#edit_movie


#delete_movie



#has an update all movies option



