class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def print_status(self):
        print(f"{self.name} has {self.health} health level left.")

    def attack(self, enemy):
        enemy.health -= self.power
        return enemy.health

    def alive(self):
        if self.health > 0:
            return True
        return False

hero = Character("Hero", 10, 5)
goblin = Character("Goblin", 6, 2)
options = """
1. fight goblin
2. do nothing
3. flee
"""

def main():
    if goblin.alive() and hero.alive():
        print (options)
        hero.print_status()
        goblin.print_status()
        user_input = int(input("What do you want to do? "))
        if user_input == 1:
            # Hero attacks goblin
            hero.attack(goblin)
            # conditional outcomes of attack    
            if not goblin.alive():
                print ("The goblin is dead.")
                
        elif user_input == 2:
            pass
        elif user_input == 3:
            print ("Goodbye.")   
        else:
            print ("Invalid input %d") % user_input
            main()
    
    if hero.alive() and goblin.alive():
        goblin.attack(hero)     
        if not hero.alive():
            print ("You are dead.")
    
    if hero.alive() and goblin.alive():
        main()

main()