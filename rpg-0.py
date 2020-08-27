import random
import time

class Character:
  def __init__(self,name, health, power, coins):
    self.name = '<undefined>'
    self.health = health
    self.power = power
    self.coins = coins

  def alive (self):
    if self.health > 0:
      return True
    else:
      return False 

  def attack(self, enemey):
    enemey.health -= self.power
    print(f'{self.name} did {self.power} damage to {enemey.name}')    

  def print_status(self):
    print(f'{self.name} has {self.health} health and {self.power} power.')  


class Hero(Character):
  def __init__(self):
    self.name = 'Alex'
    self.health = 10
    self.power = 5

  def attack(self, enemey):
      double_damage = random.random() < 0.2
      if double_damage:
        enemey.health -= self.power * 2 
        


class Goblin(Character):
  def __init__(self):
    self.name = 'Pepe'
    self.health = 6
    self.power = 2




class Medic(Character):
  def __init__(self):
    self.health = 'Medic'
    self.health = 10
    self.power = 5

  def receive_damage(self, points):
    self.health -= points
    print(f'{self.name} received {points} damage.')
    recuperate = random.random() < 0.2
    if recuperate:
      self.health += 2
    if self.health <= 0:
      print(f'{self.name} is dead.')

class Shadow(Character):
  def __init__(self):
    self.name = 'Shadow'
    self.health = 1
    self.power = 5

  def receive_damage(self, points):
    if random.random() >= 0.10:
      print("Shadow didn't take damage.")
    else:
      self.health -= points
      print(f'{self.name} received {points} damage.') 
      if self.health <= 0:
        print(f'{self.name} is dead.')

  

hero = Hero()
goblin = Goblin()
options = '''
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
'''

def main():
  while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print(options)
    user_input = input('What do you want to do? ')
    if user_input == "1":
        # Hero attacks goblin
        hero.attack(goblin)
        if goblin.alive() == False:
            print("The goblin is dead.")
    elif user_input == "2":
        pass
    elif user_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)

    if goblin.health > 0:
        # Goblin attacks hero
        goblin.attack(hero)
        if hero.health <= 0:
            print("You are dead.")

main()