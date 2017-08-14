# By Edwin Aquino - Aug. 13, 2017
# https://github.com/edwinaquino/movietrailers
# My Favorite Movie Trailers By Edwin Aquino
import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and hist toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://youtu.be/5PSNL1qE6VY?t=10s")

departed = media.Movie(
    "The Departed",
    "An undercover cop and a mole in the police department",
    "http://www.freemovieposters.net/posters/departed_the_2006_1253_poster.jpg",   # noqa
    "https://www.youtube.com/watch?v=auYbpnEwBBg")

matrix = media.Movie(
  "The Matrix",
  "A group of free humans battle machine",
  "http://www.overimage.com/temp/matrix2.jpg",
  "https://www.youtube.com/watch?v=vKQi3bBA1y8")

rush_hour = media.Movie(
    "Rush Hour",
    "East meets West in this racial, buddy-cop comedy.",
    "http://static.cinemagia.ro/img/db/movie/00/01/89/rush-hour-798893l.jpg",
    "https://www.youtube.com/watch?v=rs_6Psn1XK0")

fellowship_of_the_ring = media.Movie(
    "The Fellowship of the Ring",
    " Tolkien's classic fantasy novel.",
    ("http://www.overimage.com/temp/ring.jpg"),
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

movies = [
    matrix,
    rush_hour,
    fellowship_of_the_ring,
    toy_story,
    avatar,
    departed
]

fresh_tomatoes.open_movies_page(movies)
