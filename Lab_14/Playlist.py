from ChainingHashTableMap import ChainingHashTableMap

class PlayList:
    def __init__(self):
        self.hashmap = ChainingHashTableMap()
        self.first_song = ""
        self.last_song = ""

    def add_song(self, new_song_name):
        if self.hashmap.is_empty():
            self.first_song = new_song_name
        
        self.hashmap[self.last_song] = new_song_name
        self.last_song = new_song_name
        self.hashmap[new_song_name] = ""

    def add_song_after(self, song_name, new_song_name):
        after = self.hashmap[song_name]

        self.hashmap[song_name] = new_song_name
        self.hashmap[new_song_name] = after

        if after == "":
            self.last_song = new_song_name

    def play_song(self, song_name):
        if self.hashmap[song_name]:
            print("Playing " + song_name)
        else:
            raise KeyError("Song not in playlist")

    def play_list(self):
        curr = self.hashmap[self.first_song]
        print("Playing " + self.first_song)

        while curr != "":
            print("Playing " + curr)
            curr = self.hashmap[curr]

p1 = PlayList( )
p1.add_song("Jana Gana Mana")
p1.add_song("Kimi Ga Yo")
p1.add_song("The Star-Spangled Banner")
p1.add_song("March of the Volunteers")

p1.add_song_after("The Star-Spangled Banner", "La Marcha Real") 
p1.add_song_after("Kimi Ga Yo", "Aegukga")
p1.add_song("Arise, O Compatriots")
p1.add_song("Chant de Ralliement")
p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
p1.add_song_after("Jana Gana Mana", "God Save The Queen")

p1.play_song("The Star-Spangled Banner")
p1.play_song("Jana Gana Mana")
p1.play_list( )

'''
Expected Output: 
"Playing The Star-Spangled Banner"
"Playing Jana Gana Mana"
"Playing Jana Gana Mana"
"Playing God Save The Queen"
"Playing Kimi Ga Yo"
"Playing Aegukga"
"Playing The Star-Spangled Banner"
"Playing La Marcha Real"
"Playing March of the Volunteers" 
"Playing Arise, O Compatriots" 
"Playing Chant de Ralliement" 
"Playing Himno Nacional Mexicano"
'''