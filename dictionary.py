import time
album = {
    'title' : "Ta13oo",
    'artist' : "Denzel Curry",
    'genre' : "Hip Hop",
    'release_date' : "July 27, 2018",
    'runtime' : "43:20",
    'tracks' : "13",
    'songs': ["Taboo", "Black Balloons", "Cash Maniac", "Sumo", "Super Saiyan Superman", "Switch It Up", "Mad I Got It", "Sirens", "Clout Cobain", "The Blackest Balloon", "Percs", "Vengeance", "Black Metal Terrorist",]
    }

for key, value in album.items():
        print("%s:%s"%(key,value))
while True:
        user_input = input("Choose a Song or type exit to leave ").lower()
        
        
        if user_input == 'exit':
                user_input == input("Goodbye")
                
        for i in range(0,3):
                print("Playing Song...")
                time.sleep(1)


