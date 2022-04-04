###############################################################################    
# This file was made to test the PokerScorer Class methods.
#
###############################################################################    
# Imports, variables, objects used in testing.
###############################################################################
import pygame
import CardClass
import PokerScorerClass
pygame.init()
pygame.display.set_mode((640, 480))
pygame.display.set_caption("Texas Hold 'Em")
scorer = PokerScorerClass.PokerScorer()
hand1 = list()
hand2 = list()
table = list()
###############################################################################
            ######  MODIFY THESE APPENDS TO TEST THE SCORER  ######
###############################################################################
## 1st testing hand ##
hand1.append(CardClass.Card("6","s"))
hand1.append(CardClass.Card("6","c"))
## 2nd Testing hand ##
hand2.append(CardClass.Card("11","s"))
hand2.append(CardClass.Card("10","s"))
## Cards on the Table ##
table.append(CardClass.Card("1","h"))
table.append(CardClass.Card("1","d"))
table.append(CardClass.Card("4","d"))
table.append(CardClass.Card("4","c"))
table.append(CardClass.Card("8","c"))

print("Pair: ", scorer.pair(hand1, table))
print("Two Pair: ", scorer.twoPair(hand1, table))
print("3 of Kind: ", scorer.threeOfAKind(hand1, table))
print("Straight: ", scorer.straight(hand1, table))
print("FLUSH: ", scorer.flush(hand1, table))
print("Full House: ", scorer.fullHouse(hand1, table))
print("4 of a kind: ", scorer.fourOfAKind(hand1, table))
print("Straight Flush: ", scorer.straightFlush(hand1, table))
print("Royal Flush: ", scorer.royalFlush(hand1, table))