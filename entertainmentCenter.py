import media
import fresh_tomatoes


# Store the information of a movie
# that will be opened by our website
# \ used to break up long lines
sausage_party = media.Movie("Sausage Party",
                            "Supermarket food learns about their brutal fate",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcQccZ--X\
                            qJZcX5RTwlCy1_WJTyOUb_50xUS5cIzVdmOZtCNtIfu",
                            "http://www.youtube.com/watch?v=WVAcTZKTgmc")

shaolin_soccer = media.Movie("Shaolin Soccer",
                             "Using kung fu to play football",
                             "http://www.gstatic.com/tv/thumb/movieposter"
                             "s/30276/p30276_p_v8_ae.jpg",
                             "https://www.youtube.com/watch?v=6FAaOwNnHTA")

hitman_bodyguard = media.Movie("The Hitman's Bodyguard",
                               "A bodyguard is called to protect a hitman",
                               "http://t3.gstatic.com/images?q=tbn:ANd9G\
                               cRp9f9X9bK3mxhMNxYTXbjSx7WlFmG3gEYQj\
                               K8bS7xncQJFpqVt",
                               "https://www.youtube.com/watch?v=F4Afusxc2SM")

get_out = media.Movie("Get Out",
                      "Guy meets his girlfriedns parents",
                      "https://i.ytimg.com/vi/YfLSryEaAfw/movieposter.jpg",
                      "https://www.youtube.com/watch?v=A2JbO9lnVLE")


deadpool = media.Movie("Deadpool",
                       "A film about an anti-hero",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcTvrIHJfa\
                       sS6poy34esN1O5hZonXaiqfEZb4WbnbAa9qJCIL8_9",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

stomp_the_yard = media.Movie("Stomp the Yard",
                             "A black joins a fraternity a university",
                             "http://www.gstatic.com/tv/thumb/dvdboxart/16"
                             "2827/p162827_d_v8_aa.jpg",
                             "https://www.youtube.com/watch?v=hvLzhK7Vatw")


movies = [sausage_party, shaolin_soccer, hitman_bodyguard,  get_out, deadpool,
          stomp_the_yard]
fresh_tomatoes.open_movies_page(movies)
