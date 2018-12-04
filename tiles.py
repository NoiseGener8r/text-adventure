import items, enemies

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()
         
    def modify_player(self, player):
        raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """You find yourself in a small round cave. Light streaks down from somewhere far above, and you can make out a small passage to the north."""

    def modify_player(self, player):
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        the_player.hp = the_player.hp - self.enemy.damage
        print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

### Tiles ###

class BonesRoom(LootRoom):
    def __init__(self, x, y)_:
        super(),__init__(x, y, items.Stick())

    def intro_text(self):
        return """You enter a small chamber. A pile of bones, rocks, and other assorted garbage lies in the corner. You notice a hefty-looking stick and pick it up."""

class SlimeRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(self, x, y, enemies.Slime())

    def intro_text(self):
        if self.enemy.is_alive():
            return """A large cave room filled with strange globular things. You reach down to inspect one, when it suddenly jumps up at you!"""
        else:
            return """A large cave room filled with strange globular things. One lies in several pieces on the ground in the middle of the room."""

class EmptyHall(MapTile):
    def intro_text(self):
        return """A long empty hall."""

    def modify_player(self, player):
        pass


