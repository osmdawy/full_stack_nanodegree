import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story","A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://imgc.allpostersimages.com/images/P-473-488-90/89/8919/KXDR300Z/posters/toy-story-woody-buzz.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
monsters = media.Movie("Monsters,Inc","In order to power the city, monsters have to scare children so that they scream. However, the children are toxic to the monsters, and after a child gets through, two monsters realize things may not be what they think.",
                       "http://concertposter.org/-2013Mar/Monsters-Inc/Monsters-Inc-All-TeaserNT-drop.jpg",
                       "https://www.youtube.com/watch?v=8IBNZ6O2kMk")
Beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "Belle, whose father is imprisoned by the Beast, offers herself instead, unaware her captor to be an enchanted prince.",
                                   "https://www.movieposter.com/posters/archive/main/17/A70-8828",
                                   "https://www.youtube.com/watch?v=tRlzmyveDHE")

my_neighbor = media.Movie("My Neighbor Totoro",
                          "When two girls move to the country to be near their ailing mother, they have adventures with the wonderous forest spirits who live nearby.",
                          "http://ecx.images-amazon.com/images/I/51i0O8MNsfL.jpg",
                          "https://www.youtube.com/watch?v=TuLX50_5UAI")
coraline = media.Movie("Coraline",
                       "An adventurous girl finds another world that is a strangely idealized version of her frustrating home, but it has sinister secrets.",
                       "https://movieposteraddict.files.wordpress.com/2008/11/mpacoralineposter2b.jpg",
                       "https://www.youtube.com/watch?v=LO3n67BQvh0")
frozen = media.Movie("Frozen","When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.",
                     "http://vignette2.wikia.nocookie.net/disney/images/5/58/Frozen-movie-poster.jpg/revision/latest?cb=20131002122858",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

#adding all movies to a new list called movies
movies = [toy_story,monsters,Beauty_and_the_beast,my_neighbor,coraline,frozen]
#call open from fres_tomatoes module to create the html file and open it
fresh_tomatoes.open_movies_page(movies)
print media.Movie.__doc__
