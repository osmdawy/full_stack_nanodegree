import webbrowser
class Movie():
   
    """This is a Movie class to create any movie with the paramater to constructor movie title,movie story line,movie poster and the trailer url"""
    def __init__(self,movie_title,movie_storyline,movie_poster,trailer_youtube):
        #instance variables for movie object
        self.title =movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_youtube
        
