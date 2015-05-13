import unittest
import sys
sys.path.insert(0, '../')
from movie import *

# class MovieTestCase(unittest.TestCase):
# 	def test_movie_create
b = Movie(title="Frozen",imdbID = "tt2294629")

b.get_omdb_data()
print b.content_to_html(), b.omdb_data["Poster"]
response = Movie.search_omdb_by_title('Age of Ultron')

print response