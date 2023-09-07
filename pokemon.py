import random
from os import system, name

white = "\033[0;37m"
cyan="\033[1;36m" 
green="\033[0;92m"
orange = "\033[0;33m"
pink = "\033[1;31m"
blue="\033[1;34m"
yellow = "\033[0;93m"
red = "\033[0;31m"
light_red = "\033[1;31m"
purple = "\033[0;35m"
# Define some basic Pokémon attributes
pokemon1 = {"name": f"{yellow}Pikachu{white}", "type": f"{yellow}Electric{white}", "hp": 100, "attack": 20, "maxhp": 100, "ascii_art": 
f'''{yellow}
       \:.             .:/
        \``._________.''/ 
         \             / 
 .--.--, / .':.   .':. \\
/__:  /  | '::' . '::' |
   / /   |`.   ._.   .'|
  / /    |.'         '.|
 /___-_-,|.\  \   /  /.|
      // |''\\.;   ;,/ '|
      `==|:=         =:|
         `.          .'
         :-._____.-:
          `''       `''
{white}'''}

pokemon2 = {"name": f"{red}Charmander{white}", "type": f"{red}Fire{white}", "hp": 100, "attack": 25, "maxhp": 100, "ascii_art":
f'''{red}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠊⠉⠁⠒⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⡊⠁⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⣴⣶⣀⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣏⡏⠀⠀⠀⠀⠀⠀⠀⡼⢉⠟⣆⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠞⠛⠀⠀⠀⠀⠀⠀⠀⢰⠗⠊⠀⢸⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⣀⣀⡞⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀
⠀⠀⠀⠘⣦⣀⠁⠀⠀⠂⠀⠀⠀⠀⠀⢀⣀⣀⡴⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣼⢿⠀⠀⠀
⠀⡟⠓⠤⣘⣿⣿⡒⠒⠶⠒⠒⠚⠋⣿⣉⠽⢋⠆⠀⠀⡄⠀⠀⠀⣀⡤⠶⣶⠀⠀⠀⠀⠀⢠⣿⠉⢀⡈⠷⢿⠀
⢾⡻⣏⠀⠀⠉⠻⣷⣦⠤⠤⠤⠤⢾⣯⣵⡞⠁⠀⠀⠘⠓⠒⠉⠉⠀⠉⡿⠿⣤⠀⠀⠀⠀⠀⢻⣧⣼⡇⠀⢸⡄
⠀⠑⢄⠀⠀⠀⠀⠀⢹⠏⠀⠈⠉⠁⠀⠈⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⢀⡿⢿⣧⣄⠀⢷
⠀⠀⠀⠱⣄⠀⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀⠀⠀⣀⡴⠃⠀⠀⠀⠀⠀⠀⠀⣸⠀⠈⣿⣿⣆⡼
⠀⠀⠀⠀⠈⠓⢤⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠒⠲⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⢈⣿⠃
⠀⠀⠀⠀⠀⠀⠀⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⡞⢻⠋⠀
⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⣾⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⢰⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣀⡀⣀⡀⡿⠦⢄⣀⣀⣀⠤⠴⠊⠁⠀⢠⡟⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡞⠁⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣴⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⢀⡿⠑⠒⠀⣏⠀⠀⠀⠀⠀⠀⠀⣟⣒⠒⠒⠒⣊⣩⠔⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⡤⠖⠚⠻⣶⠀⠀⠀⠀⢯⡀⠀⠀⠀⢘⡆⠀⠀⠀⠀⣠⡞⠁⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣾⣟⣱⢦⡀⠀⠀⠀⠀⣀⣀⣨⠇⠀⠀⠀⢸⢀⡀⢀⣀⢀⣉⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢉⣉⡉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠘⢿⣸⣿⣸⣿⣼⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{white}'''}

# Function to calculate damage
def calculate_damage(attacker, defender):
  effectiveness = 1.0
  miss = random.randint(1, 6)
  if miss == 1:
    print(f"{attacker['name']}'s attack missed!")
    return 0
  if attacker["type"] == "Electric" and defender["type"] == "Water":
    effectiveness = 2.0
  elif attacker["type"] == "Water" and defender["type"] == "Fire":
    effectiveness = 2.0
  elif attacker["type"] == "Fire" and defender["type"] == "Grass":
    effectiveness = 2.0
  elif attacker["type"] == "Grass" and defender["type"] == "Electric":
    effectiveness = 2.0

  damage = (attacker["attack"] + 5* random.randint(-2,2)) * effectiveness
  return int(damage)
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')
clear()
# Main battle loop
def runpokemon(p1,p2):
  while p1["hp"] > 0 and p2["hp"] > 0:
    # clear()
    print(p1["ascii_art"])
    print(
        f"{p1['name']} {green}(HP: {p1['hp']}){white} vs. {p2['name']} {green}(HP: {p2['hp']}){white}"
    )
  
    # Pokemon 1 attacks Pokemon 2
    print(f"What to do?: {light_red}[Attack]   {green}[Heal]    {purple}[Gamble]{white}: ")
    attack = input()
  
    if attack == "Attack":
      damage_to_p2 = calculate_damage(p1, p2)
      p2["hp"] -= damage_to_p2
      print(f"{p1['name']} attacks {p2['name']} for {red}{damage_to_p2}{white} damage!")
  
    if attack == "Heal":
      damage_to_p1 = random.randint(10, 50)
      p1["hp"] = min(100, p1["hp"]+damage_to_p1)
      print(f"{p1['name']} heals himself for {green}{damage_to_p1}{white} health!")
  
    if attack == "Gamble":
      damage_to_p1 = (calculate_damage(p1, p1) * 2)
      damage_to_p2 = (calculate_damage(p1, p2) * 2)
      
      roulette=random.randint(1, 2)
  
      if roulette == 1:
        p2["hp"] -= damage_to_p2
        print(f"{p1['name']} attacks {p2['name']} for {red}{damage_to_p2}{white} damage!")
      else:
        p1["hp"] -= damage_to_p1
        print(f"{p1['name']} attacks himself for {red}{damage_to_p1}{white} damage!")
  
    if p2["hp"] <= 0:
      print(f"{p2['name']} fainted!")
      break
  
    # Pokemon 2 attacks Pokemon 1'
    if p2["hp"] < p2["maxhp"]/2:
      damage_to_p2 = random.randint(10, 50)
      p2["hp"] += damage_to_p2
      print(f"{p2['name']} heals himself for {green}{damage_to_p2}{white} health!")
    else:
      damage_to_p1 = calculate_damage(p2, p1)
      p1["hp"] -= damage_to_p1
    
      print(
          f"{p2['name']} attacks {p1['name']} for {red}{damage_to_p1}{white} damage!"
      )
  
    if p1["hp"] <= 0:
      print(f"{p1['name']} fainted!")
    input(f'{cyan}>')
    clear()
  # Determine the winner
  if p1["hp"] <= 0:
    clear()
    print(f"{p2['name']} wins!")
  elif p2["hp"] <= 0:
    clear()
    print(f"{p1['name']} wins!")
  else:
    clear()
    print("It's a tie!")
  
  print("The battle is over.")


print(f"{yellow}Pikachu: Electric")
print(f"{pokemon1['ascii_art']}")
print(f"{red}Charmander: Fire{white}")
print(f"{pokemon2['ascii_art']}")
char=input("Which Pokemon do you wish to select: ")
clear()
if char == "Pikachu":
  runpokemon(pokemon1,pokemon2)
else:
  runpokemon(pokemon2,pokemon1)


  
