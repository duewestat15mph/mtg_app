import pandas as pd
import json
import random
deckPath = "Inputs/deck.csv"
# Data pulled from https://mtgjson.com/downloads/all-files/#allidentifiers
cardPath = "C:\pythonProject\mtg_app\Data\AllIdentifiers.json"


class CustomError(Exception):
    pass


class theCards:
    def __init__(self, deckPath):
        self.cardList = []
        self.cardlistStatic = None
        self.deckDict = {}
        self.graveyard = []
        self.discard = []
        self.hand = []
        self.deckDict = {}
        self.round = 0

        deckData = pd.read_csv(deckPath)
        f = open(cardPath, encoding='utf-8')
        cardData = json.load(f)

        legalDeck = True
        deckSize = 0
        deckSet = set(deckData['Card'])

        for key in cardData['data'].keys():
            if cardData['data'][key]['name'] in deckSet:
                self.deckDict[cardData['data'][key]['name']] = cardData['data'][key]
                deckSet.remove(cardData['data'][key]['name'])

        for index,row in deckData.iterrows():
            if row['Card'] not in self.deckDict.keys():
                legalDeck = False
                print(f"You have a card in your deck that does not appear to be legal:\n{row['Card']}\n")
            else:
                deckSize += row['Count']
                for x in range(0,row['Count']):
                    self.cardList.append(row['Card'])

        self.cardlistStatic = tuple(self.cardList)


        if not legalDeck:
            raise CustomError("Not using a legal deck")

        self.drawPile = self.shuffle_draw()
        self.hand = self.draw_cards(7)

    def shuffle_draw(self):
        theList = self.cardlistStatic
        theList = list(theList)
        for x in self.discard:
            theList.remove(x)
        for x in self.graveyard:
            theList.remove(x)

        shuffled = []
        while len(theList) > 0:
            pick = random.randint(0, len(theList)-1)
            shuffled.append(theList[pick])
            theList.pop(pick)

        return shuffled

    def draw_cards(self, n=1):
        theDraw = []
        for x in range(0,n):
            theDraw.append(self.drawPile[0])
            self.drawPile.pop(0)
        return theDraw

    def mulligan(self):
        handSize = len(self.hand)
        if handSize >= 4 and self.round == 0:
            self.drawPile = self.shuffle_draw()
            self.hand = self.draw_cards(handSize - 1)
        elif self.round != 0:
            print("This is only available before the first round")
        elif handSize < 4:
            print("Your hand does not have enough cards for a mulligan")

    def next_round(self):
        self.round += 1
        self.hand = self.hand + self.draw_cards(1)

    def playCard(self,cardNumber,location):
        self.hand.pop(cardNumber)




class tableTop:
    def __init__(self):
        self.hitPoints = 20
        self.manaAvailable = {
            'red':0,
            'colorless':0,
            'green':0,
            'blue':0,
            'black':0,
            'white':0
        }
        self.creatures = []

