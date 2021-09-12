import random
print("Welcome to the game! You will be playing against an A.I.")
print("Here are the attacks that you will be able to use: ")
print("[1] Quick Attack: Gives 11 to 16 damage to the opponent")
print("[2] Slow attack: Gives 26 to 37 damage to the opponent, BUT you might lose the round becouse he might repel it!")
print("[3] Spell : With this action, you will heal yourself by 8 to 12 hp and damage the opponent by five")
print("You both start with 100 health points")
print("Whoever wins 2 rounds first, wins the fight.")
print("Are you ready to play?")
ready = input("Y/N: ")

turn = 1
Round = 1
PlayerHealth = 100
AiHealth = 100
KeepPlaying = True
AiRoundWins = 0
PlayerRoundWins = 0


if ready == "n" or ready == "N":
    print("Okay then!")
elif ready == "y" or ready == "Y":
    print("")
    print("--------------------------------------------")
    print("Let the fight begin!")
    print("")
    print("The A.I. goes first.")
    print("--------------------------------------------")
    while KeepPlaying == True:
        if (turn % 2) == 1:
            print("It is the A.I's turn: ")
            print("")
            if Round == 1:                                      #round one ai does only quick attacks
                damage = random.randint(11,16)
                PlayerHealth = PlayerHealth - damage
                if PlayerHealth < 0:
                    PlayerHealth = 0
                print("The A.I. performed a Qick attack and damaged you by ", damage, " health points!")
                print("Your current health: " , PlayerHealth)
                print("A.I's current health: ", AiHealth)
                turn = turn + 1
            elif Round == 2:
                AttackKind = random.randint(1,3)
                if AiHealth <= 25:                                   #ai spell if hp too low
                    SpellHealth = random.randint(8,12)
                    AiHealth = AiHealth + SpellHealth
                    if AiHealth > 100:
                        AiHealth = 100
                    print("The A.I. performed a spell! It healed itself by ", SpellHealth, " health points.")
                    print("Your current health: " , PlayerHealth)
                    print("A.I's current health: ", AiHealth)
                    turn = turn + 1
                else:
                    if AttackKind == 1:                           #ai quick attack
                        damage = random.randint(11,16)
                        PlayerHealth = PlayerHealth - damage
                        if PlayerHealth < 0:
                            PlayerHealth = 0
                        print("The A.I. performed a Qick attack and damaged you by ", damage, " health points!")
                        print("Your current health: " , PlayerHealth)
                        print("A.I's current health: ", AiHealth)
                        turn = turn + 1
                        
                    elif AttackKind == 2:                            #ai slow attack
                        LoseRound = random.randint(1,2)
                        if LoseRound == 1:
                            print("The A.I. tried to perform a slow attack but you repeled it! Good job!")
                            turn = turn + 1
                        else:
                            damage = random.randint(26,37)
                            PlayerHealth = PlayerHealth - damage
                            if PlayerHealth < 0:
                                PlayerHealth = 0
                            print("The A.I. performed a slow attacka and hit you! It damaged you by: ", damage, " health points")
                            print("Your curent health: ", PlayerHealth)
                            print("A.I.'s current health: ", AiHealth)
                            turn = turn + 1
                            
                    elif AttackKind == 3:                              #ai spell
                        SpellHealth = random.randint(8,12)
                        AiHealth = AiHealth + SpellHealth
                        if AiHealth > 100:
                            AiHealth = 100
                        print("The A.I. performed a spell! It healed itself by ", SpellHealth, " health points.")
                        print("Your current health: " , PlayerHealth)
                        print("A.I's current health: ", AiHealth)
                        turn = turn + 1
            
            elif Round == 3:
                AttackKind = random.randint(1,3)
                if AiHealth <= 40:                                   #ai spell if hp too low
                    SpellHealth = random.randint(8,12)
                    AiHealth = AiHealth + SpellHealth
                    if AiHealth > 100:
                        AiHealth = 100
                    print("The A.I. performed a spell! It healed itself by ", SpellHealth, " health points.")
                    print("Your current health: " , PlayerHealth)
                    print("A.I's current health: ", AiHealth)
                    turn = turn + 1
                else:
                    if AttackKind == 1:                           #ai quick attack
                        damage = random.randint(11,16)
                        PlayerHealth = PlayerHealth - damage
                        if PlayerHealth < 0:
                            PlayerHealth = 0
                        print("The A.I. performed a Qick attack and damaged you by ", damage, " health points!")
                        print("Your current health: " , PlayerHealth)
                        print("A.I's current health: ", AiHealth)
                        turn = turn + 1
                        
                    elif AttackKind == 2:                            #ai slow attack
                        LoseRound = random.randint(1,2)
                        if LoseRound == 1:
                            print("The A.I. tried to perform a slow attack but you repeled it! Good job!")
                            turn = turn + 1
                        else:
                            damage = random.randint(26,37)
                            PlayerHealth = PlayerHealth - damage
                            if PlayerHealth < 0:
                                PlayerHealth = 0
                            print("The A.I. performed a slow attacka and hit you! It damaged you by: ", damage, " health points")
                            print("Your curent health: ", PlayerHealth)
                            print("A.I.'s current health: ", AiHealth)
                            turn = turn + 1
                            
                    elif AttackKind == 3:                              #ai spell
                        SpellHealth = random.randint(8,12)
                        AiHealth = AiHealth + SpellHealth
                        if AiHealth > 100:
                            AiHealth = 100
                        print("The A.I. performed a spell! It healed itself by ", SpellHealth, " health points.")
                        print("Your current health: " , PlayerHealth)
                        print("A.I's current health: ", AiHealth)
                        turn = turn + 1
        else:
            print("")
            print("It's now your turn!")
            print("Press [1] for Quick Attack, [2] for Slow attack, or [3] for a Spell.")
            print("You can also press [Q] to quit." )
            print("You've got this!")
            print("")
            Again = True
            while (bool(Again) == True):
                print("----------------------------------------------------------------------------")
                choice = str(input("What do you choose? : "))
                
                if choice == str(1):                                  #player quick attack
                    damage = random.randint(11,16)
                    AiHealth = AiHealth - damage
                    if AiHealth < 0:
                        AiHealth = 0
                    print("You performed a Quick attack! You damaged the A.I. by ", damage, " health points.")
                    print("Your current health: " , PlayerHealth)
                    print("A.I's current health: ", AiHealth)
                    turn = turn + 1
                    Again = False
                elif choice == str(2):                                 #player slow attack
                    LoseRound = random.randint(1,2)
                    if LoseRound == 1:
                        print("You performed a slow attack!")
                        print("Oh no, the A.I. repeled the attack! That means you didn't do any damage!")
                        print("Your current health: " , PlayerHealth)
                        print("A.I's current health: ", AiHealth)
                        turn = turn + 1
                        Again = False
                    else:  
                        damage = random.randint(26,37)
                        AiHealth = AiHealth - damage
                        if AiHealth < 0:
                            AiHealth = 0
                        print("You perfomed a slow attack and damaged the A.I. by ", damage, " health points.")
                        print("Your current health: " , PlayerHealth)
                        print("A.I's current health: ", AiHealth)
                        turn = turn+1
                        Again = False
                elif choice == str(3):                            #player spell
                    SpellHealth = random.randint(8,12)
                    PlayerHealth = PlayerHealth + SpellHealth
                    if PlayerHealth > 100:
                        PlayerHealth = 100
                    print("You performed a spell! You healed yourself by ", SpellHealth, " health points.")
                    print("Your current health: " , PlayerHealth)
                    print("A.I's current health: ", AiHealth)
                    turn = turn + 1
                    Again = False
            
                elif choice == "Q" or choice == "q":                   #player quit
                    KeepPlaying = False
                    print("Turns out you don't want to play anymore. What a shame! The A.I. wins.")
                    Again = False
                else:
                    print("Not an acceptable option. Choose again.")
                    Again = True


        if KeepPlaying == True:
            if PlayerHealth <= 0:
                AiRoundWins = AiRoundWins + 1
                print("")
                print("Oh no! A.I. wins this round!")
                
                if (AiRoundWins == 2) or (PlayerRoundWins == 2):                 #whoever has 2 wins fisrt, wins the fight
                    KeepPlaying = False
                else:
                    if Round <= 3:
                        Round = Round + 1
                        print("")
                        print("-------------------------------------------")
                        print("")
                        print("Round: ", Round - 1, " is over.")
                        print("Round: ", Round, " starts now!")
                        PlayerHealth = 100
                        AiHealth = 100
                    else:
                        KeepPlaying = False
                        
            if AiHealth <= 0:
                PlayerRoundWins = PlayerRoundWins + 1
                print("")
                print("You win this Round!")
                if (AiRoundWins == 2) or (PlayerRoundWins == 2):
                    KeepPlaying = False
                else:
                    if Round < 3:
                        Round = Round + 1
                        print("")
                        print("-------------------------------------------")
                        print("")
                        print("Round: ", Round - 1, " is over.")
                        print("Round: ", Round, " starts now!")
                        PlayerHealth = 100
                        AiHealth = 100
                        
                    else:
                        KeepPlaying = False
                        
                        
if PlayerRoundWins > AiRoundWins:                              #checking who won
    print("--------------------------------")
    print("")
    print("You won the fight! The A.I. is defeated.")
    print("The score was: ")
    print("   You: ", PlayerRoundWins)
    print("   A.I.: ", AiRoundWins)
else:
    print("--------------------------------")
    print("")
    print("The A.I. won the fight. You have been defeated.")
    print("The score was: ")
    print("   You: ", PlayerRoundWins)
    print("   A.I.: ", AiRoundWins)
    
                
                    
