# Base Character class
import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} has healed for {amount}! HP remaining: {self.health}/{self.max_health}")
  
    

 


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    def power_atk(self, opponent):  # Add your power attack method here
        damage = random.randint(self.attack_power * 2  - 10, self.attack_power * 2 + 10)
        opponent.health -= damage
        print(f"{self.name} deals damage to {opponent.name} for {damage} damage")
        if opponent.health <= 0 :
            print(f"{opponent.name} is stumbling!!") 
    def heal(self, amount):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for 5 points.  Current health: {self.health}/{self.max_health}")

    

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35) 
        self.invun = False
         
# Add your cast spell method here

    def cast_spell(self, opponent):
        
        damage = random.randint(self.attack_power * 3 - 15, self.attack_power * 3 + 15)
        opponent.health -= damage
        print(f"{self.name} cast Frost bolt on {opponent.name} and does {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} is frozen!")

    def teleport(self):
        self.invun = True
        print(f"{self.name} has teleported for one turn")


#Define Archer Class

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=40)
        self.invun = False

    def quick_shot(self, opponent):
         damage = random.randint(self.attack_power * 2 - 10, self.attack_power *2 + 10)
         opponent.health -= damage
         print(f"{self.name} slings a Quick Shot on {opponent.name} for {damage} damage!")
         if opponent.health <= 0:
             print(f"{opponent.name} is pinned down!")

     # Define evade 
    def evade(self):
        self.invun = True
        print(f"{self.name} picks up speed!")


# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=30)
        self.block = False


    def holy_strike(self, opponent):
        damage = random.randint(self.attack_power * 2 -10, self.attack_power *2 + 10)
        opponent.health -= damage
        print(f"{self.name} strikes {opponent.name} with Holy Strike for {damage} damage ")
        if opponent.health <= 0:
            print(f"{opponent.name} is stumbling!")
    def divine_shield(self):
        self.block = True
        print(f"{self.name} uses divide shield to block the attack!")

# Define Rogue
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.void = False

    def backstab(self, opponent):
         damage = random.randint(self.attack_power * 2 -10, self.attack_power *2 + 10)
         opponent.health -= damage
         print(f"{self.name} sneaks in for a backstab and hits {opponent.name} for {damage} damage!")
         if opponent.health <= 0:
             print(f"{opponent.name} isn't looking too good!")

    def into_the_void(self):
        self.void = True
        print(f"{self.name} enters into the void to miss the next attack!")
    
    
    
    

# Define Necromancer
class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=15)
        self.seed = False
        self.summon = False

    def summon_minions(self, opponent):
        self.summon = True
        damage = random.randint(self.attack_power * 2 - 10, self.attack_power *2 + 10)
        opponent.health -= damage
        print(f"{self.name} has summoned Minions for support. Minions attack for {damage}!")
        if opponent.health <= 0:
            print(f"Minions over power {opponent.name}!")

    def leach_seed(self, opponent):
        self.seed = True
        damage = random.randint(self.attack_power * 3 - 15, self.attack_power * 3 + 15)
        opponent.health -= damage
        self.health += damage // 2
        self.health = self.max_health
        print(f"{self.name} has drained {opponent.name} health by {damage} and has gained {damage // 2} HP from Leach Seed")
        if opponent.health <= 0:
            print(f"Earth has overgrown the {opponent.name}!")
        




    
    
    
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power if need be
        self.max_health = 150 
        
    # Evil Wizard's special ability: can regenerate health
    def regenerate(self):
        
        self.health += 5 
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    # Define wizard attack method that handles special abilities
    def attack(self, opponent):
        # Mage's teleport special ability
        if isinstance(opponent, Mage) and opponent.invun:
    
            

            print(f"{opponent.name} avoids the attack due to teleport!")
            opponent.invun = False  # Reset invulnerability
            return

        # Archer's evasion special ability
        elif isinstance(opponent, Archer) and opponent.invun:
            print(f"{opponent.name} evades the attack with grace!")
            opponent.invun = False  # Reset evasion
            return

        # Paladin's block special ability
        elif isinstance(opponent, Paladin) and opponent.block:
            print(f"{opponent.name} blocks the attack!")
            opponent.block = False  # Reset block ability
            return

        # Rogue's void special ability
        elif isinstance(opponent, Rogue) and opponent.void:
            print(f"{opponent.name} enters the void, attack misses!")
            opponent.void = False  # Reset void ability
            return

        elif isinstance(opponent, Necromancer) and opponent.seed:
           print(f"{opponent.name} sprouted seedlings from the Earth!  Healing {opponent.name} and consuming life from {self.name}")
           opponent.seed = False #Reset leech seed
            
            # return 
        else:
            damage = random.randint(self.attack_power * 2 - 5, self.attack_power * 2 + 5)
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} with a fire whip for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")





# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    print("5. Rogue")
    print("6. Necromancer")
    
    class_choice = input("Enter the number of your perferred adventurer: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    elif class_choice == "5":
        return Rogue(name)
    elif class_choice == '6':
        return Necromancer(name)
       
        
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        skip_enemy_turn = False #Hopefully this helps skip attacks when take specific calls for it

        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            # player.attack(wizard)
            if isinstance(player, Warrior):
                player.power_atk(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
            elif isinstance(player, Rogue):
                player.backstab(wizard)
            elif isinstance(player, Necromancer):
                player.summon_minions(wizard)
        elif choice == '2':
            if isinstance (player,Warrior):
                # player.power_atk(wizard)
                player.heal(5)
            elif isinstance(player,Mage):
                # player.cast_spell(wizard) #Should only teleport
                player.teleport()
                # skip_enemy_turn = True
            elif isinstance(player, Archer):
                # player.quick_shot(wizard)
                player.evade()
                skip_enemy_turn = True
            elif isinstance(player, Paladin):
                # player.holy_strike(wizard)
                player.divine_shield()
                skip_enemy_turn = True
            elif isinstance(player, Rogue):
                player.into_the_void()
                # player.backstab(wizard)
            elif isinstance(player, Necromancer):
                # player.summon_minions()
                player.leach_seed(wizard)
        elif choice == '3':
            player.heal(15)
        elif choice == '4':  #view stats
            player.display_stats()
            skip_enemy_turn = True
        else:
            print("Invalid choice, try again.")
            continue

        # != 4 is to be sure the wizard doesnt attack while viewing stats.
        if wizard.health > 0 and choice != '4':
            wizard.regenerate()
            if wizard.health > 0:
                wizard.attack(player)
       
        

        # if player.health <= 0:
        #     print(f"{player.name} has been defeated!")
        #     break  ## I think this is causing an extra player.name has been defeated to be printed in terminal. 

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()



