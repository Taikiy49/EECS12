# pokerapp.py

from dice import Dice

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        startValue = inputValue()
        while not(startValue <= 1000 and startValue >= 1):
            startValue = inputValue()
        self.money = startValue
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        self.interface.close()

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

def inputValue():
    startValue = input("what is the initial amount of money?")
    try:
        startValue = int(startValue)
    except:
        startValue = inputValue()
    return startValue