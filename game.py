import gamefunctions
shop_inventory = [
    {"name": "sword", "type": "weapon","powerBoost": 3, "hits": 7, "equipped":True, "price": 45},
    {"name": "blocker","type": "shield","powerBoost": 2, "hits": 5 , "equipped":True, "price":25},
    {"name": "cat", "type":"sidekick","powerBoost":4, "hits": 80, "equipped":False,"price":0},
    {"name": "nutella","type":"food", "eaten":True, "price": 50, "powerBoost": 6, "effect": "auto_defeat_monster", "equipped":True},
    {"name": "apple", "type": "food", "eaten":True, "price": 20, "powerBoost": 1, "equipped":True},
    {"name": "potion", "type": "food", "eaten":True, "powerBoost": 2, "price": 35}
]
state = {
    "player_name":"Humphrey",
    "your_dablooms": 7000,
    "player_pockets": [
        {"name": "sword","type": "weapon","powerBoost": 3, "hits": 7 , "currentHits": 7, "equipped":True},
        {"name": "blocker","type": "shield","powerBoost": 2, "hits": 5 , "currentHits": 5, "equipped":True},
        {"name": "nutella","type": "food", "powerBoost": 6, "effect": "auto_defeat_monster", "equipped":True}
        ]
}
gamefunctions.print_shop_menu(shop_inventory)
gamefunctions.shop("cat")
gamefunctions.fight_monster(10, state["your_dablooms"])
def main():
    your_health = 10
    your_dablooms = 25
    while True:
        print("You are at the castle.")
        print(f"Your current health: {your_health}")
        print(f"Your current dablooms: {your_dablooms}")
        print("What would you like to do?")
        print("1)Infilatrate Castle (fight monster)")
        print("2)Eat (restore 5 health)")
        print("3)Stop playing")

        choice = input("Choose 1-3: ")
        if choice == "1":
            gamefunctions.fight_monster(your_health,your_dablooms)
        elif choice == "2":
            gamefunctions.eat(your_health, your_dablooms)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Choose a number between 1 and 3. Try again.")
if __name__ == "__main__":
    main()
                

