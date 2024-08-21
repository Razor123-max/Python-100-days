
print(''' 
      

  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba, 
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88         8PP""""""" 
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa 
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"' 
                                                                           
                                                                           
                                                               
 88           88                                 88  
 ""           88                                 88  
              88                                 88  
 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8 

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')

print("\nWelcome to Treasure Island!!\nYour mission is to find the treasure.")

choice1 = input("\nYou are at a cross road. Where do you want to go?\ntype 'left' or 'right'.").lower()

if choice1 == "left":
    choice2 = input('\nYou\'ve come to a lake. There is an island in the middle of the lake.' 
          'Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    
    if choice2 == "wait":
        choice3 = input('\nYou\'ve arrived at the island unharmed.\nThere is a house with 3 doors. One red, one yellow, and one blue.\nWhich color do you choose?').lower()

        if choice3 == "red":
            print("\nCongratulations! You found the treasure!")
        elif choice3 == "yellow":
            print("\nYou were eaten by a crocodile.\nGame Over.")
        else:
            print("\nThe door is locked and you can't open it.\nGame Over.")

    else:
        print("\nYou got attacked by a angry trotum. Game Over.")

else:
    print("\nFall into a hole.\nGame Over.")
