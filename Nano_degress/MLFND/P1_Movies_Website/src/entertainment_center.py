import fresh_tomatoes
import media

"""
Author: Vishwajit B.
The purpose of this code is to simply create nine media or movie objects with given parameters.
It then creates a media list and populates the list with these movie objects. After the list
is populated, open_movies_page(thisList) from fresh_tomatoes module is called.
"""
ai= media.Media("Artificial Intelligence",
                        "A highly advanced robotic boy longs to become 'real'",
                        "https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
                        "https://www.youtube.com/watch?v=_19pRsZRiz4")

chowka = media.Media("Chowka",
                      "Four individuals, each with their own aspirations, land up in jail. ",
                      "https://upload.wikimedia.org/wikipedia/en/9/96/Chowka_Poster.jpg",
                      "https://www.youtube.com/watch?v=Ugkm8vr0myQ")

ulidavaru = media.Media("Ulidavaru Kandante",
                      "Four lives cross beacuse of a mysterious relic.",
                      "https://upload.wikimedia.org/wikipedia/en/5/52/Movie_Poster_of_Ulidavaru_Kandanthe.jpg",
                      "https://www.youtube.com/watch?v=POJ_6EtGeMw")

ugramm = media.Media("Ugramm",
                      "A bloody gangster and a naive girl",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/Ugramm_audio.jpeg/220px-Ugramm_audio.jpeg",
                      "https://www.youtube.com/watch?v=qmQEt_MQaLA")


iRobot = media.Media("I, Robot",
                      "A technophobic cop investigates murder.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg",
                      "https://www.youtube.com/watch?v=rL6RRIOZyCM")

minority_report = media.Media("Minority Report",
                      "A Story of precogs and precrime officer.",
                      "https://upload.wikimedia.org/wikipedia/en/4/44/Minority_Report_Poster.jpg",
                      "https://www.youtube.com/watch?v=jdl6eAIx2K4")

children_heaven = media.Media("Children of Heaven",
                      "Adventurous story of a boy who loses shoes of his sister.",
                      "https://upload.wikimedia.org/wikipedia/en/f/f7/Children_of_heaven.jpg",
                      "https://www.youtube.com/watch?v=dqxvZeQsVzY")

tropic_thunder = media.Media("Tropic Thunder",
                      "A group of actors get in trouble in hilarius ways.",
                      "https://upload.wikimedia.org/wikipedia/en/d/d6/Tropic_thunder_ver3.jpg",
                      "https://www.youtube.com/watch?v=9Pl4JNnqNaE")

great_debaters = media.Media("The Great Debaters",
                      "A True story based on professor Melvin B.Tolson",
                      "https://upload.wikimedia.org/wikipedia/en/f/f5/Great_debaters_post.jpg",
                      "https://www.youtube.com/watch?v=IN2AGZThL-8")

#Populate the array with nine Media objects
media_arr = [ai, minority_report, iRobot, ulidavaru, ugramm, chowka, children_heaven, great_debaters, tropic_thunder]
#Call open_movies_page to create fresh_tomatoes.htm
fresh_tomatoes.open_movies_page(media_arr)



