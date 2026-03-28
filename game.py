import gamefunctions

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
                
    
