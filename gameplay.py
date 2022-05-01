from classes import theCards, tableTop


def roundZero(deckPath):
    deck = theCards(deckPath)
    print("Here is your hand...")
    mulligan = True
    while(mulligan):
        land = ""
        creatures = ""
        other = ""
        for x in deck.hand:
            if 'Land' in deck.deckDict[x]['types']:
                land += "{:<30} | {:<15} \n".format(x, ",".join(deck.deckDict[x]['types']))
            elif 'Creature' in deck.deckDict[x]['types']:
                creatures += "{:<30} | {:<15} \n".format(x, ",".join(deck.deckDict[x]['types']))
            else:
                other += "{:<30} | {:<15} \n".format(x, ",".join(deck.deckDict[x]['types']))
        print(land + creatures + other)

        mulligan = input("Would you like to re-draw your hand at the cost on one card? (Y/N)")

        if mulligan.lower()[0] == 'y':
            deck.mulligan()
            mulligan = True
        else:
            mulligan = False
    return deck

def manaPhase(deck, tableTop):
    hasLand = []
    for x in range(0,len(deck.hand)):
        print("{}|{:<30} | {:<15}".format(x, deck.hand[x], ",".join(deck.deckDict[deck.hand[x]]['types'])))
        if 'Land' in deck.deckDict[deck.hand[x]]['types']:
            hasLand.append(x)

    if len(hasLand) > 0:
        temp = ','.join(str(s) for s in hasLand)
        playland = input(f"Would you like to a land card? ({temp})")
        while int(playland) not in hasLand:
            playland = input(f"I'm afraid that's not a land card.\nWould you like to a land card? ({temp})")
        deck.playcard(playland)
        tableTop.playMana()

    else:
        print("you have no land cards to play.  Press any key to continue")

def roundN(deck, tabletop):
