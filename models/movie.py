import re
import urllib
import urllib2
import json, ast
import cgi
import yaml
import uuid


class Movie:
    def __init__(self,title = '',
        trailer_youtube_url = '', 
        imdbID ='',
        omdb_data='',
        poster_url='',
        index =''):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.imdbID = imdbID
        if omdb_data == '':
            self.omdb_data = {}
            self.get_omdb_data()
        else:
            self.omdb_data = omdb_data
        if index == '' and 'imdbID' in self.omdb_data.keys():
            self.index = self.omdb_data['imdbID']
        elif index != '':
            self.index = index
        else:
            index = uuid.uuid4()
            self.index =  str(index)
        if poster_url == '' and "Poster" in self.omdb_data.keys():
    	   self.poster_url = self.omdb_data["Poster"]
        else:
            self.poster_url = poster_url
        if "Title" in self.omdb_data.keys():
           self.title = self.omdb_data["Title"]
        self.youtube_id()
    @classmethod
    def table(self):
        return 'movies'


    def nice_yaml(self):
        return {'title': str(self.title), 
        'index': str(self.index),
        'trailer_youtube_url': self.trailer_youtube_url,
        'imdbID': str(self.imdbID),
        'poster_url': str(self.poster_url),
        'omdb_data': ast.literal_eval(json.dumps(self.omdb_data)) }

    def content_to_html(self):
        return ('''
        <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{self.trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
            <img src="{self.poster_url}" width="220" height="342">
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
        try: 
            results = json.loads(response.read())["Search"]
        except: 
            results = []
        return results   

    @classmethod
    def choose_from_results(self,results):
        num = [-1]
        movie_data = None
        def next_movie():
            num[0] += 1
            return results[num[0]]         
        while len(results) -1  > num[0]:
            current_movie = next_movie()
            for  key,value in  current_movie.iteritems():
                print ( key + ': ' + value )
            ismovie = raw_input("Is this your movie?: Yes/No  ")
            if len(ismovie) >= 1 and ismovie.lower()[0] == "y":
                movie_data = current_movie
                break
            print "----------------------------"
        return movie_data

    @classmethod
    def get_index_content(self, data):
        content = ''
        for key,movie in data.iteritems():
            content += movie.content_to_html()
        return content

class Blog(Movie):
    pass




