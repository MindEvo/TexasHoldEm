##############################################################################
# Card Class
#   Creates a poker card object for use with Pygame library.
##############################################################################
# Member variables
#   string type; suit
#   string type; value
#   string type; card
##############################################################################
import ImageSpriteClass as ISC

class Card:
###############
# CONSTRUCTOR #
###############    
    def __init__(self, value, suit):
    ###########################################################################
    #  Initialize the card with a suit (c,d,h,s) and value (1-13).
    #   Both parameters should be entered as string types.
    ###########################################################################    
        self._suit = str(suit)
        self._value = str(value)
        self._cardName = str(value + suit)
        self._imgFile = str("D:/CompSci/Projects/Python Poker/DECK/" + 
                            self._cardName + ".gif")
        self._backImgFile = str("D:/CompSci/Projects/Python Poker/DECK/b.gif")
        self._sprite = ISC.ImageSprite(50,100, self._imgFile)

############
# MUTATORS #
############
    def moveCard(self, x, y):
    ###########################################################################    
    # Use to move the card throughout the display/window
    ###########################################################################    
       self._sprite.moveTo(x,y)

    def hide(self):
    ###########################################################################    
    # Use to display the back of the card, hide the value/suit.
    ###########################################################################    
        self._sprite.kill()
        self._sprite = ISC.ImageSprite(50, 100, self._backImgFile)
        
    def show(self):
    ###########################################################################    
    # Use to show the front of the card, the value and suit.
    ###########################################################################    
        self._sprite.kill()
        self._sprite = ISC.ImageSprite(50,100, self._imgFile)
        
#############
# ACCESSORS #
#############
    def getSuit(self):
        return self._suit 

    def getValue(self):
        return self._value
    
    def getCardName(self):
        return self._cardName
    
    def getImageFile(self):
        return self._imgFile
    
    def getSprite(self):
        return self._sprite

    def getBackSprite(self):
        return self._backSprite

#############
# OPERATORS #
#############
    def __lt__(self, other):
        return self._value < other._value
    
    def __gt__(self, other):
        return self._value > other._value
    
    def __eq__(self, other):
        return self._value == other._value
    
    