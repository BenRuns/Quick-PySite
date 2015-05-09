import re
class Movie:
    def __init__(self,title = '',poster_image_url='',trailer_youtube_url = ''):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    	self.youtube_id()
    def content(self):
        return '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{self.trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{self.movie_title}</h2>
</div>
'''

    def youtube_id(self):
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        self.trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None


b = Movie()
print b.content()
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



