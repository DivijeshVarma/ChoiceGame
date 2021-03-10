# python Game

print("Welcome to Game")

name = input("What is your Name? ")
age = int(input("What is your Age? "))

points = 20

if age >= 18:
    # weapon = input("To play the game choose weapon (axe/hammer): ")
    print("You entered Game with 20 points")
    choice = input("make a choice left or right (left/right): ")
    if choice == 'left':
        lft = input('You entered into Forest and heard stange\
noises (run/hide): ')
        if lft == 'run':
            print("you were atacked by Tiger and lost 10 points")
            points -= 10
            inpp = input("escaping from tiger (tree/bushes): ")
            if inpp == 'tree':
                print("you were atacked by Tiger and lost 10 points")
                points -= 10
                if points == 0:
                    print("you have 0 points and lost game")
                else:
                    print("you survived")
            else:
                print(f"you were safely returned home with {points}")
        elif lft == 'hide':
            hd = input("Tribe people are passing by (meet/hide): ")
            if hd == 'meet':
                print("you were injured by Tribe people and lost 10 points")
                points -= 10
                if points == 0:
                    print("you have 0 points and lost game")
                else:
                    print("you survived")
            elif hd == 'hide':
                print('you found a way home and you won the Game. '
                      f'with {points} points')
    elif choice == 'right':
        rht = input("you found a strange house and river (house/river): ")
        if rht == 'house':
            print("stranger attacks you and lost 10 points")
            points -= 10
            if points == 0:
                print("you have 0 points and lost game")
            else:
                print("you survived")
        elif rht == 'river':
            input('you crossed river, reached home '
                  f'and won Game with {points}')

else:
    print(f"{name}, you are not allowed because of age restriction")
