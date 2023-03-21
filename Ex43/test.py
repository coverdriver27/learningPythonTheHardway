class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


class Engine:
    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()

        while True:
            print("\n" + "-" * 20)
            print(current_room.name + "\n")
            print(current_room.description)

            if current_room == self.room_map.ending_room():
                print("\nCongratulations! You have reached the end of the game.")
                break

            direction = input("\nWhere would you like to go next? ")
            current_room = current_room.go(direction)


class Map:
    def __init__(self, start_room, end_room):
        self.start_room = start_room
        self.end_room = end_room

    def opening_room(self):
        return self.start_room

    def ending_room(self):
        return self.end_room

    def add_room(self, room):
        setattr(self, room.name.lower().replace(" ", "_"), room)


# define your game map here
start_room = Room("Start Room",
                  "You wake up in a dimly lit room. The air is damp and musty. You can't remember how you got here.")
middle_room = Room("Middle Room", "This room is filled with cobwebs and dust. You can barely see anything.")
end_room = Room("End Room", "You made it to the end of the game! Congratulations!")

start_room.add_paths({"north": middle_room})
middle_room.add_paths({"south": start_room, "east": end_room})
end_room.add_paths({"west": middle_room})

game_map = Map(start_room, end_room)
game_map.add_room(start_room)
game_map.add_room(middle_room)
game_map.add_room(end_room)

# run the game
game_engine = Engine(game_map)
game_engine.play()
