# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        player = f"{self.name}'s items:\n"
        for n, item in enumerate(self.items, start=1):
            player += f"   {n}. {item.name}\n"

        return player

    def move(self, room):
        self.current_room = room

    def collect_item(self, item):
        self.items.append(item)
        item.on_take()
