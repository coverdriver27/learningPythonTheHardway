"""
Exercise 40 : Modules Classes and Objects
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# print(">>>>1")
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So i'll stop right there"])
# print(">>>>2")

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

lakers_anthem = Song(["""The Lakers are magnificent
Critics better admit it
We winning, shoot it, pivot
With less than a second left and it swishes
Don’t test us, you know how vicious"""])

var1 = """Its, your Birthday,
You get any gift you like
just go out to the gift shop
and swipe that card you gotcha name on it"""

happy_bday.sing_me_a_song()
print("\n")
lakers_anthem.sing_me_a_song()
print("\n")
bulls_on_parade.sing_me_a_song()

print("\n -------------Using variables------------------------ \n")
print(var1)
print("\n")
# var1.sing_me_a_song() ---> Wont work
# we get a attribute error : AttributeError: 'str' object has no attribute 'sing_me_a_song'
