class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(
                name="Gold",
                description="A small round coin with {} stamped on the side.".format(str(self.amt)),
                value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().init(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Stick(Weapon):
    def __init__(self):
        super().init(
                name="Stick"
                description="A short, thick stick suitable for hitting things with."
                value=1
                damage=3
                )







