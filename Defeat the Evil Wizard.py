import random
from abc import ABC, abstractmethod

# Base Character class
class Character(ABC):
    @abstractmethod
    def __init__(self, name, health, attack_power):
        #attributes, charateristics or properties of object
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
#methods, acitons or behaviors that can be performed
    def attack(self, opponent): 

        #Unique attacking abilities

        if hasattr(opponent, 'block') and opponent.block: 
            print(f"{opponent.name} successfully blocked the attack!")
            opponent.block = False #Reset block after use

        elif hasattr(opponent,'evade') and opponent.evade: 
            print(f"{opponent.name} has succesffulyy dodged the attack!")
            opponent.evade = False

        elif hasattr(opponent,'self_heal') and opponent.self_heal:
            print(f"{opponent.name} has successfully healed and cancelled the attack!")
            opponent.self_heal = False

        else:
           
            min_damage = self.attack_power
            max_damage = max(60,self.attack_power)

            damage = random.randint(min_damage, max_damage)
            opponent.health -= damage

            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has been defeated!")

    def heal(self):
        if self.health >= self.max_health:
            print('You cannot go over your health limit')
        else:
            healed_amount = min(30, self.max_health - self.health) #prevent overhealing
            self.health += healed_amount
            print(f'{self.name} used heal! Gained {healed_amount} HP. Current Health: {self.health}/{self.max_health}')

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
#polymorphism - allow to override superclass method for specific implementation
    def attack(self, opponent):
        print(f"{self.name} swings a mighty axe at {opponent.name}!")
        damage = random.randint(self.attack_power, self.attack_power + 15)
        opponent.health -= damage
        print(f"{self.name} dealt {damage} damage to {opponent.name}!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name, self_heal):
        super().__init__(name, health=100, attack_power=35)
        self.self_heal = False

    def attack(self, opponent):
        print(f"{self.name} casts a fireball at {opponent.name}!")
        damage = random.randint(self.attack_power + 5, self.attack_power + 20)
        opponent.health -= damage
        print(f"{self.name} burned {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    #Mage unique ability to heal
    def heal_on_attack(self):
        self.self_heal = True
        print(f"You cannot knock me down! Self Heal!!")
        healing_HP = random.randint(3,6)
        self.health += healing_HP
        print( f" {self.name} new HP: {self.health}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name, unique_ability):
        super().__init__(name, health=150, attack_power=15)
        self.unique_ability = unique_ability
       

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    #Summoning minions
    def summon_spawns(self, opponent):
        print(f"\tYou will have to fight harder if you want to take me down! {self.unique_ability} arise!!!")
        print(f"\nI hope you are ready {opponent.name}!")
        damage = random.randint(self.attack_power, self.attack_power + 7)
        opponent.health -= damage
        print(f"-{self.name}'s minions have hit you with attacks from all over for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")


# Create Archer class
class Archer(Character):
    def __init__(self, name, unique_attack, evade):
        super().__init__(name, health = 200, attack_power = 5)
        self.unique_attack = unique_attack
        self.evade = False 

    def attack(self, opponent):
        print(f"{self.name} quickly fires an arrow at {opponent.name}!")
        damage = random.randint(self.attack_power * 3, self.attack_power * 6)
        opponent.health -= damage
        print(f"{self.name} hit {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

#Unique abilities
    def use_ability(self, opponent):
        opponent.health -= self.attack_power*5
        new_damage = self.attack_power*5
        print(f'{self.name} has used the {self.unique_attack}!(double arrow attack): For {new_damage} damage')
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def evading(self,opponent): 
        self.evade = True
        print(f"{self.name} is very quick and is preparing to dodge the Wizards next attack")
        
     
   

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name, unique_attack,block):
        super().__init__(name, health = 100, attack_power = 20)
        self.unique_attack = unique_attack 
        self.block = False

    def attack(self, opponent):
        print(f"{self.name} swings their holy sword at {opponent.name}!")
        damage = random.randint(self.attack_power, self.attack_power * 2)
        opponent.health -= damage
        print(f"{self.name} struck {opponent.name} with divine power for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

#Unique abilities
    def cast_spell(self,opponent):
        opponent.health -= self.attack_power*3
        new_damage = self.attack_power*3
        print(f'{self.name} has used the {self.unique_attack} (Holy Strike)!: For {new_damage} damage')
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def use_shield(self,opponent):
            self.block =True
            print(f"{self.name} has blocked the Evil Wizards attack after raising their shield")

    


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ").upper()

    if class_choice == '1':
        return Warrior(name) #This is an instance of warrior class? #yes
    elif class_choice == '2':
        return Mage(name,'Self Heal')
    elif class_choice == '3':
        # Implement Archer class
        return Archer(name,'Quick shot','Evade') 
    elif class_choice == '4':
        return Paladin(name,'Cast spell','Block')  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    



def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1': 
            player.attack(wizard) 
        elif choice == '2':
            if isinstance(player,Archer):
                player.use_ability(wizard)#polymorphism to call method
                player.evading(wizard)
            elif isinstance(player,Paladin): 
                player.cast_spell(wizard)
                player.use_shield(wizard)

            elif isinstance(player,Mage):
                player.heal_on_attack()
            else:
                print("This Character has no special ability")
        elif choice == '3':
            player.heal()  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
 #wizard.unique_attack(player) minions feature
        if wizard.health > 50 and wizard.health < 70:
            wizard.summon_spawns(player)
          
            


        if player.health <= 0:
            print( f"The quest continues to find the chosen one that can defeat {wizard.name}")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}! Victory is yours! You saved the village of Narnia.")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard", 'Minions') 
    battle(player, wizard) 

if __name__ == "__main__": 
    main()
