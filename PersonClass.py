##############################################################################
# Person Class
#   Creates a person object.
##############################################################################
# Member variables
#   string type;            name
#   int type;               bank
#   list of cards type;     hand
##############################################################################

class Person:
###############
# CONSTRUCTOR #
###############
    def __init__(self, name, bank):
    ###########################################################################
    # Initialize the person object.
    #   Takes a string parameter for their name.
    #   Takes an integer parameter for how much money they have.
    #   Hand is list of card type objects.
    ###########################################################################
        self._name = name
        self._bank = bank
        self._hand = list()


############
# MUTATORS #
############
    def addMoney(self, amount):
    ###########################################################################
    # Parameter amount is an int. Add money to a person's bank.
    ###########################################################################
        self._bank = self._bank + amount
        
    def removeMoney(self, amount):
    ###########################################################################
    # Parameter amount is an int. Remove money from person's bank.
    ###########################################################################
        self._bank = self._bank - amount

    def addCard(self, card):
    ###########################################################################
    # Parameter is Card type object. Adds a card to the person hand variable,
    #   which is a list of Card type objects.
    ###########################################################################
        self._hand.append(card)
        
    def removeCards(self):
    ###########################################################################
    # No parameters.
    #   Removes the cards from the players hand by moving them off screen, and
    #   then clearing the list. Don't worry about memory since the cards are
    #   able to be pulled on to the screen when they are needed.
    ###########################################################################
        for i in range(len(self._hand)):
            self._hand[i].moveCard(3000,3000)
        self._hand = list()
        
    def hideCard(self, index):
    ###########################################################################
    # Switches the card face to the card back.
    ###########################################################################
        self._hand[index].hide()
        
    def showCard(self, index):
    ###########################################################################
    # Switches the card back to the card face.
    ###########################################################################
        self._hand[index].show()
        
#############
# ACCESSORS #
#############
    def getMoney(self):
        return self._bank
    
    def getCard(self, index):
        return self._hand[index]

    def getHand(self):
        return self._hand