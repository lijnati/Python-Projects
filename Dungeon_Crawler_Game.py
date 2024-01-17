'''

https://github.com/lijnati/Python-Projects


In this 1D Dungeon Crawler Game, the player starts with 100 health. They can choose to fight a monster, which starts with 50 health, or try to run away.

During the fight, the player can choose to attack, defend, or run away. The attack will deal random damage between 1 and 10, while the defend option will decrease the player's health by a random amount between 1 and 5.

The game ends when the player runs out of health. If the player successfully runs away, the game ends without further action. If the player fails to run away, they will be forced to fight.

Please note that this game does not have any predefined stages or a map, it's a simplified example of a 1D Dungeon Crawler Game.

'''



import random

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

def fight(player, monster):
    while player.is_alive() and monster.is_alive():
        print(f"{player.name} has {player.health} health.")
        print(f"{monster.name} has {monster.health} health.")
        print("Choose an action:")
        print("1) Attack")
        print("2) Defend")
        print("3) Run")

        action = input("> ")

        if action == "1":
            monster.health -= random.randint(1, 10)
            print(f"{player.name} attacks {monster.name} for {random.randint(1, 10)} damage.")
        elif action == "2":
            player.health -= random.randint(1, 5)
            print(f"{player.name} defends and takes {random.randint(1, 5)} damage.")
        elif action == "3":
            if random.random() > 0.5:
                print(f"{player.name} manages to run away.")
                return
            else:
                print(f"{player.name} fails to run away.")

        if player.is_alive() and monster.is_alive():
            print(f"{monster.name} attacks {player.name} for {random.randint(1, 10)} damage.")
            player.health -= random.randint(1, 10)

def main():
    player = Player("Hero", 100)
    monster = Monster("Monster", 50)

    while player.is_alive():
        print(f"{player.name} has {player.health} health.")
        print("Choose an action:")
        print("1) Fight")
        print("2) Run")

        action = input("> ")

        if action == "1":
            fight(player, monster)
        elif action == "2":
            if random.random() > 0.5:
                print(f"{player.name} manages to run away.")
                return
            else:
                print(f"{player.name} fails to run away.")

if __name__ == "__main__":
    main()