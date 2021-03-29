################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope (exists in functions)
def drink_potion():
  posion_stength = 2
  print(posion_stength)

drink_potion()
#print(potion_strength)

# Global scope
player_health = 10

def game():
  def drink_potion_global():
    posion_stength = 2
    print(player_health)

  drink_potion_global()
print(player_health)