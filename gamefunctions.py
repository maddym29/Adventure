import random
shop_inventory = [
    {"name": "sword" ,"type": "weapon","powerBoost": 3, "hits": 7, "currentHits": 7, "equipped":True, "price": 45},
    {"name": "blocker","type": "shield","powerBoost": 2, "hits": 5 , "currentHits": 5,  "equipped":True, "price":25},
    {"name": "cat", "type":"sidekick","powerBoost":4, "hits": 80, "equipped":False,"price":0},
    {"name": "nutella","type":"food", "equipped":True, "powerBoost": 6, "effect": "auto_defeat_monster", "price": 50},
    {"name": "apple", "type": "food", "equipped":True, "price": 20},
    {"name": "potion", "type": "food", "equipped":True, "powerBoost": 2, "price": 35}
]
state = {
    "player_name":"Humphrey",
    "your_dablooms": 7000,
    "player_pockets": [
        {"name": "sword","type": "weapon","powerBoost": 3, "hits": 7 , "currentHits": 7, "equipped":True},
        {"name": "blocker","type": "shield","powerBoost": 2, "hits": 5 , "currentHits": 5, "equipped":True},
                {"name": "nutella","type": "food","equipped":True, "effect": "auto_defeat_monster", "powerBoost": 6}
        ]
}
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
def equip():
    print("What type of item would you like to equip?")
    item_type = input("Type (weapon, shield, food): ").lower()
    
    matching_items = []
    for item in state["player_pockets"]:
        if item.get("type") == item_type:
            matching_items.append(item)
    if not matching_items:
        print("Invalid 'type' choice. Try again.")
        return
    
    print(f"\nYour {item_type}s:")
    
    for i, item in enumerate(matching_items, start=1):
        print(f"{i}) {item['name']}")

    choice = int(input("Choose an item number: "))
    if 1 <= choice <= len(matching_items):
        chosen_item = matching_items[choice - 1]
        for item in state["player_pockets"]:
            if item.get("type") == item_type:
                item["equipped"] = False
        chosen_item["equipped"] = True
        print(f"You equipped the {chosen_item['name']}!")
        if "powerBoost" in chosen_item:
            print(f"You gained +{chosen_item['powerBoost']} power boost.")
        if "effect" in chosen_item:
            print(f"The effect: {chosen_item['effect']}.")
    else:
        print("Invalid choice.")

def print_shop_menu(shop_inventory):
    """
    This function creates a bordered menu.
        Paramaters:
            shop_inventory(int and str)
    """
    print("//--------------------\\")
    for item in shop_inventory:
        print(f"| {item['name']:<12}${item['price']:>7.2f} |")
    print("\\--------------------//")

def get_equipped_weapon():
    for item in state["player_pockets"]:
        if item.get("type") == "weapon" and item.get("equipped") == True:
            return item
    return None

def get_auto_defeat_item():
    for item in state["player_pockets"]:
        if item.get("effect") == "auto_defeat_monster":
            return item
    return None

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
        print("3) Equip power-up")

        action = input("Choose 1 - 3: ")

        if action == "1":

            defeat_item = get_auto_defeat_item()
            if defeat_item:
                print(f"You used {defeat_item['name']}. The monster is instantly defeated!")
                monster_health = 0
                state["player_pockets"].remove(defeat_item)
                break
            weapon = get_equipped_weapon()
            if weapon:
                powerBoost = weapon.get("powerBoost", 0)
                weapon["currentHits"] -= 1
                print(f"Your {weapon['name']} looses 1 durability. Remaining hits: {weapon['currentHits']}")
                if weapon["currentHits"] <= 0:
                    print(f"Your {weapon['name']} breaks!")
                    state["player_pockets"].remove(weapon)
            else:
                powerBoost = 0
            damage_to_monster = random.randint(1, 6)
            total_damage = damage_to_monster + powerBoost
            monster_health -= total_damage
            damage_to_player = random.randint(1, 4)
            your_health -= damage_to_player

            print(f"You stabbed the monster for {damage_to_monster}!")
            if monster_health > 0:
                damage_to_player = random.randint(1,4)
                your_health -= damage_to_player
            print(f"The monster hits you for {damage_to_player}!")
            print(f"Your health: {your_health} | Monster health: {monster_health}")

        elif action == "2":
            print("You escaped!")
            return your_health, your_dablooms
        elif action == "3":
            equip()
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

def shop(item_name):
    print(state["your_dablooms"])
    print(state["player_pockets"])
    for object in shop_inventory:
        if object["name"] == item_name:
            if state["your_dablooms"] >= object["price"]:
                state["your_dablooms"] -= object["price"]
                state["player_pockets"].append(object.copy())
                print("You bought(a)", item_name)
            else:
                print("Not enough dablooms.")


def equip():
    print("What type of item would you like to equip?")
    item_type = input("Type (weapon, shield, food): ").lower()
    
    matching_items = []
    for item in state["player_pockets"]:
        if item.get("type") == item_type:
            matching_items.append(item)
    if not matching_items:
        print("Invalid 'type' choice. Try again.")
        return
    
    print(f"\nYour {item_type}s:")
    
    for i, item in enumerate(matching_items, start=1):
        print(f"{i}) {item['name']}")

    choice = int(input("Choose an item number: "))
    if 1 <= choice <= len(matching_items):
        chosen_item = matching_items[choice - 1]
        for item in state["player_pockets"]:
            if item.get("type") == item_type:
                item["equipped"] = False
        chosen_item["equipped"] = True
        print(f"You equipped the {chosen_item['name']}!")
        if "powerBoost" in chosen_item:
            print(f"You gained +{chosen_item['powerBoost']} power boost.")
        if "effect" in chosen_item:
            print(f"The effect: {chosen_item['effect']}.")
    else:
        print("Invalid choice.")

        
    
    
    
