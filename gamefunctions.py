import random
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    max_affordable = startingMoney // itemPrice
    if max_affordable < quantityToPurchase:
        items_bought = max_affordable
    else:
        items_bought = quantityToPurchase
    money_left = startingMoney - (items_bought * itemPrice)
    return items_bought, money_left
def new_random_monster():
    monsters = ["Giraffe Bear", "Smoothie Butterfly", "Kitten Dragon"]
    healthy = [3, 4, 6]
    worth = [500, 200, 400]
    name = random.choice(monsters)
    if name == "Giraffe Bear":
        description = "A cuddly creature with a long neck."
        health = random.choice([1,3,5])
        power = "Ability to reach high things and give warm hugs"
        money = random.choice([100, 300, 500])
    elif name == "Smoothie Butterfly":
        description = "A beautiful bug with strawberry banana scented wings."
        health = random.choice([2,4,6])
        power = "Ability to slurp up enemies and make a mean kale smoothie."
        money = random.choice([200, 400, 600])
    elif name == "Kitten Dragon":
        description = "A blue cat with green eyes and purple wings and tail."
        health = random.choice([6, 8, 10])
        power = "Ability to breath fire on enemies and always land on feet."
        money = random.choice([10, 20, 40])
    else:
        description = "Invalid choice."
        health = "Invalid choice."
        power = "Invalid choice."
        money = "Invalid choice."
    monster ={
        "name": name,
        "description": description,
        "health": health,
        "power": power,
        "money": money
    }     
    return monster
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    This function creates a bordered menu.
        Paramaters:
            item1Name (str): imputs first name
            item1Price (int): imputs first price (rounds to two decimal places)
            item2Name (str): imputs second name
            item2Price (int): imputs second price (rounds to two decimal places)
    """
    print ("//--------------------\\")
    print(f"| {item1Name:<12}${item1Price:>7.2f} |")
    print(f"| {item2Name:<12}${item2Price:>7.2f} |")
    print("\\--------------------//")

def fight_monster(your_health, your_dablooms):
    monster = new_random_monster()
    monster_health = monster["health"]
    
    print(f"\nA terrifying {monster['name']} emerges from the castle!")
    print(monster["description"])
    print(monster["power"])

    while your_health > 0 and monster_health > 0:
        print(f"\nYour health: {your_health} | Monster health: {monster_health}")
        print("1) Joust")
        print("2) Flee")

        action = input("Choose 1 or 2: ")

        if action == "1":
            damage_to_monster = random.randint(1, 6)
            damage_to_player = random.randint(1, 4)

            monster_health -= damage_to_monster
            your_health -= damage_to_player

            print(f"You stabbed the monster for {damage_to_monster}!")
            print(f"The monster hits you for {damage_to_player}!")

        elif action == "2":
            print("You escaped!")
            return your_health, your_dablooms
        else:
            print("Invalid Choice. Try again.")
def eat(your_health,your_dablooms):
    print_shop_menu("Apple", 5, "Potion", 10)
    choice = input("Choose from the menu (1 or 2): ")
    if choice == "1":
        if your_dablooms >= 5:
            your_dablooms -= 5
            your_health += 5
        else:
            print("Not enough dablooms!")
        return your_health, your_dablooms
    elif choice == "2":
        if your_dablooms >= 10:
            your_dablooms -= 10
            your_health += 10
        else:
            print("Not enough dablooms!")
        return your_health, your_dablooms
    else:
        print("Invalid Choice. Try again.")
    
    
    
