import media
import fresh_tomatoes

the_godfather = media.Movie("The Grandfather",
                            "One of Hollywood's greatest critical and commercial successes, The Godfather gets everything right; not only did the movie transcend expectations, it established new benchmarks for American cinema.",
                            "http://3.bp.blogspot.com/-kfFobXahgCI/T2e9e7R6uwI/AAAAAAAAAxY/tZtoOySAHKs/s1600/the-godfather-movie-poster-1020243893.jpg",
                            "https://www.youtube.com/watch?v=5DO-nDW43Ik")
print(the_godfather.storyline)

twelve_monkeys = media.Movie("12 Monkeys",
                             "The plot's a bit of a jumble, but excellent performances and mind-blowing plot twists make 12 Monkeys a kooky, effective experience.",
                             "https://weekdaymatinee.files.wordpress.com/2012/05/12-monkeys-itunes.jpg",
                             "https://www.youtube.com/watch?v=15s4Y9ffW_o")

cuckoo_nest = media.Movie("One Flew Over the Cuckoo's Nest",
                           "A criminal pleads insanity after getting into trouble again and once in the mental institution rebels against the oppressive nurse and rallies up the scared patients. ",
                           "http://4.bp.blogspot.com/-zocTOzAHvTY/TXlHS59pGOI/AAAAAAAAE28/w8C4g46mPds/s1600/one-flew-over-the-cuckoos-nest.jpg",
                           "https://www.youtube.com/watch?v=OXrcDonY-B8")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers. ",
                         "http://1l5umu3rds2b2masq81ui5c2.wpengine.netdna-cdn.com/wp-content/uploads/2013/06/music-from-the-matrix-album.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

american_beauty = media.Movie("American Beauty",
                              "A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend. ",
                              "http://eu.movieposter.com/posters/archive/main/65/MPW-32838",
                              "https://www.youtube.com/watch?v=3ycmmJ6rxA8")

gladiator = media.Movie("Gladiator",
                         "When a Roman General is betrayed, and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge. ",
                         "https://fanart.tv/fanart/movies/98/movieposter/gladiator-52f1832e56737.jpg",
                         "https://www.youtube.com/watch?v=owK1qxDselE")


movies = [twelve_monkeys, the_matrix, american_beauty, gladiator, cuckoo_nest]
fresh_tomatoes.open_movies_page(movies)

#print(twelve_monkeys.storyline)
#twelve_monkeys.show_trailer()
