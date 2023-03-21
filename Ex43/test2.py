import random


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []
        self.enemies = []

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def has_items(self):
        return bool(self.items)

    def has_enemies(self):
        return bool(self.enemies)

    def describe(self):
        print("\n" + "-" * 20)
        print(self.name + "\n")
        print(self.description)

        if self.has_items():
            print("\nThe following items are in the room:")
            for item in self.items:
                print("- " + item.name)

        if self.has_enemies():
            print("\nThere are enemies in the room!")


class Engine:
    def __init__(self, player, room_map):
        self.player = player
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()

        while True:
            current_room.describe()

            if current_room == self.room_map.ending_room() and not current_room.has_enemies():
                print("\nCongratulations! You have reached the end of the game.")
                break

            if current_room.has_enemies():
                self.player.fight(current_room.enemies)

                if not self.player.is_alive():
                    print("\nYou have died! Game over.")
                    break

                if not current_room.has_enemies():
                    print("\nYou have defeated all the enemies in the room.")

            direction = input("\nWhere would you like to go next? ")

            if direction in self.player.inventory:
                self.player.use_item(direction)

            elif direction == "inventory":
                self.player.show_inventory()

            else:
                current_room = current_room.go(direction)

                if current_room is None:
                    print("\nYou cannot go in that direction.")

                elif current_room.has_enemies():
                    self.player.fight(current_room.enemies)

                    if not self.player.is_alive():
                        print("\nYou have died! Game over.")
                        break

                    if not current_room.has_enemies():
                        print("\nYou have defeated all the enemies in the room.")

                elif current_room.has_items():
                    self.player.pick_up_items(current_room.items)
                    current_room.items.clear()


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


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.inventory = {}

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount
