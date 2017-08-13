import webbrowser
	# ACCORDING TO THE GOOGLE STYLE GUIDE FOR PHYTHO SAYS USE CAPITAL LETTER WHEN DEFINING A CLASS
	# https://google.github.io/styleguide/pyguide.html

class Movie():
	"""tthis is the documentation"""
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
