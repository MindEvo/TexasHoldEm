##############################################################################
# Deck Class
#   Creates a deck of cards object. Inherits card class.
##############################################################################
# Member variables
#   list of strings type;   deck
#   integer type;           deckIndex
##############################################################################
import CardClass as C
from random import randint

class Deck(C.Card):
###############
# CONSTRUCTOR #
###############
    def __init__(self):
    ###########################################################################    
    # Initialize the deck of cards.
    #   Takes no arguments.
    ###########################################################################    
        self._deckIndex = 0
        self._cards = [
            C.Card("1","c"),C.Card("1","d"),C.Card("1","h"),C.Card("1","s"),
            C.Card("2","c"),C.Card("2","d"),C.Card("2","h"),C.Card("2","s"),
            C.Card("3","c"),C.Card("3","d"),C.Card("3","h"),C.Card("3","s"),
            C.Card("4","c"),C.Card("4","d"),C.Card("4","h"),C.Card("4","s"),
            C.Card("5","c"),C.Card("5","d"),C.Card("5","h"),C.Card("5","s"),
            C.Card("6","c"),C.Card("6","d"),C.Card("6","h"),C.Card("6","s"), 
            C.Card("7","c"),C.Card("7","d"),C.Card("7","h"),C.Card("7","s"),
            C.Card("8","c"),C.Card("8","d"),C.Card("8","h"),C.Card("8","s"),
            C.Card("9","c"),C.Card("9","d"),C.Card("9","h"),C.Card("9","s"),
            C.Card("10","c"),C.Card("10","d"),C.Card("10","h"),C.Card("10","s"),
            C.Card("11","c"),C.Card("11","d"),C.Card("11","h"),C.Card("11","s"),
            C.Card("12","c"),C.Card("12","d"),C.Card("12","h"),C.Card("12","s"),
            C.Card("13","c"),C.Card("13","d"),C.Card("13","h"),C.Card("13","s")
            ]

#############
# ACCESSORS #
#############
    def getCard(self, index):
        return self._cards[index]
    
    def getDeckIndex(self):
        return self._deckIndex
    
############
# MUTATORS #
############
    def shuffleDeck(self):
    ###########################################################################    
    # Randomizes the order of the strings in the deck list member variable.
    ###########################################################################    
        
        ## Move index to top of deck
        self._deckIndex = 0

        ## Number of shuffles to commit.
        times = 888
        
        while times > 0:
            ## Loop through every index of the list and exchange it for a 
            #   random index in the list.
            for i in range(len(self._cards)):
                hold = self._cards[i]
                randCard = randint(0,51)
                self._cards[i] = self._cards[randCard]
                self._cards[randCard] = hold
            times = times - 1

    def drawCard(self):
    ###########################################################################    
    # Pull top card from deck, increment card index.
    ###########################################################################    
        s = self._cards[self._deckIndex]
        self._deckIndex = self._deckIndex + 1
        return s