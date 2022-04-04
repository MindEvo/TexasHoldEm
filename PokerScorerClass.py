##############################################################################
# PokerScorer Class
#   Creates a Scorer, an object that takes in card hands and scores them by
#   returning a boolean if a particular poker hand is found.
#
##############################################################################

class PokerScorer:
###############
# CONSTRUCTOR #
###############
    def __init__(self):
        self._name = "Scorer"

    def highCard(self, cardHand):
    ###########################################################################    
    # Returns the highest value card in the hand.
    ###########################################################################    
        card1 = int(cardHand[0].getValue())
        card2 = int(cardHand[1].getValue())
        if card1 == 1:
            return cardHand[0]
        if card2 == 1:
            return cardHand[1]
        if card1 > card2:
            return cardHand[0]
        else:
            return cardHand[1]

    def pair(self, cardHand, houseCards):
    ###########################################################################    
    # Looks for 2 cards with the same value.
    #   Returns true if found.
    ###########################################################################    
        cards = cardHand + houseCards

        for i in range(len(cards)):
            for j in range(i+1,len(cards)):
                if cards[j].getValue() == cards[i].getValue():
                    return True

        return False

    def twoPair(self, cardHand, houseCards):
    ###########################################################################
    # Looks for two sets of two cards with the same value.
    #   Returns true if found.
    ###########################################################################
        cards = cardHand + houseCards
        numPairs = 0
        for i in range(len(cards)):
            for j in range(i+1,len(cards)):
                if cards[j].getValue() == cards[i].getValue():
                    numPairs = numPairs + 1
        if numPairs >= 2:
            return True
        else:
            return False
        #######################################################
        # BUG (FIX APPLIED)
        #   Does not return true if three pairs exist.
        #######################################################

    def threeOfAKind(self, cardHand, houseCards):
    ###########################################################################    
    # Looks for three cards with the same value.
    #   Returns true if found.
    ###########################################################################    
        cards = cardHand + houseCards
        count = 0
        for i in range(len(cards)):
            for j in range(i+1,len(cards)):
                if cards[j].getValue() == cards[i].getValue():
                    count = count + 1
                if count == 2:
                    return True
            count = 0
        return False

    def straight(self, cardHand, houseCards):
    ###########################################################################    
    # Looks for 5 cards that have values in a sequential order
    # or a sequence of: 1, 10, 11, 12, 13.
    #   Returns true if found.
    ###########################################################################    
        cards = cardHand + houseCards
        temp = list()
        for i in range(len(cards)):
            x = cards[i].getValue()
            temp.append(int(x))
        temp.sort()
        #######################################################################
        # Check for 1,10,11,12,13 Straight
        #   If first card 1, create a set with (10,11,12,13), check if 
        #   this is a subset of the temp.
        #######################################################################
        if temp[0] == 1:
            set1 = {10,11,12,13}
            set2 = set(temp)
            if set1.issubset(set2):
                return True
        ## Remove duplicates
        temp = set(temp)
        temp = list(temp)
        #######################################################################
        ## Count number of times (value + 1) equals next value in temp. If
        #   count reaches 4 return True. Reset count to zero whenever
        #   (value + 1) does not equal next value.
        #######################################################################
        count = 0
        for i in range(len(temp)-1):
            if temp[i] + 1 == temp[i+1]:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
        ## If neither of the above tests returns true then no straight.
        return False


    def flush(self, cardHand, houseCards):
    ###########################################################################    
    # Look for 5 cards with the same suit.
    #   Returns true if found.
    ###########################################################################    
        cards = cardHand + houseCards
        suits = list()
        for i in range(len(cards)):
            x = cards[i].getSuit()
            suits.append(x)
        clubs = 0
        diamonds = 0
        hearts = 0
        spades = 0
        for i in range(len(suits)):
            if suits[i] == 'c':
                clubs = clubs + 1
            elif suits[i] == 'd':
                diamonds = diamonds + 1
            elif suits[i] == 'h':
                hearts = hearts + 1
            elif suits[i] == 's':
                spades = spades + 1
        return clubs >= 5 or diamonds >= 5 or hearts >= 5 or spades >= 5

    def fullHouse(self, cardHand, houseCards):
    ###########################################################################
    # Look for 3 cards with the same value, and two cards of same value.
    #   Return true if found.
    ###########################################################################
        if not self.threeOfAKind(cardHand, houseCards):
            return False
        else:
            cards = houseCards + cardHand
            values = list()
            for i in range(len(cards)):
                x = cards[i].getValue()
                values.append(int(x))
            values = set(values)
            if len(values) == 4:
                return True
            else:
                return False
        #############
        ## FIX BUG ##
        #################################################################
        # When reading in 3ofaKind, and two pairs, method throws false  #
        #   when it should throw true.                                  #
        #################################################################

    def fourOfAKind(self, cardHand, houseCards):
    ###########################################################################    
    # Look for 4 cards of the same value.
    #   Return true if found.
    ###########################################################################    
        cards = cardHand + houseCards
        count = 0
        for i in range(len(cards)):
            for j in range(i+1,len(cards)):
                if cards[j].getValue() == cards[i].getValue():
                    count = count + 1
                if count == 3:
                    return True
            count = 0
        return False

    def straightFlush(self, cardHand, houseCards):
    ###########################################################################    
    # Look for combination of straight and a flush.
    #
    ###########################################################################    
        return self.flush(cardHand, houseCards) and self.straight(cardHand, houseCards)
        ##################
        # BUG FIX NEEDED #
        ##################
        #######################################################################
        # Method should only return true when the 5 cards that make the flush
        # are the same 5 cards that make the straight.
        #######################################################################

    def royalFlush(self, cardHand, houseCards):
    ###########################################################################    
    # Look for 5 cards of identical suit with values of 1, 10, 11, 12, 13
    #   Returns true if found.
    ###########################################################################    
        if not self.straightFlush(cardHand, houseCards):
            return False
        if self.highCard(cardHand, houseCards).getValue == "1":
            return True
        else:
            return False
        ##################
        # BUG FIX NEEDED #
        ##################
        #######################################################################
        # Method should return false for the 1,2,3,4,5 straight.
        #######################################################################
        
    def tieBreaker(self, score, playerHand, computerHand, houseCards):
    ###########################################################################    
    # Take score as a string argument. Check if player or computer has
    #   the higher card in the winning hand.
    #
    #                ########################
    #                # METHOD IS INCOMPLETE #
    #                ########################
    # Needs implementations for:
    #    "Flush"
    #    "Full House"
    #    "Four of a Kind"
    #    "Straight Flush"
    #    "Royal Flush"
    ###########################################################################    
        playerCards = playerHand + houseCards
        computerCards = computerHand + houseCards

        if score == "High Card":
            playerHighCard = self.highCard(playerHand)
            computerHighCard = self.highCard(computerHand)

        elif score == "Pair":
            for i in range(len(playerCards)):
                for j in range(i+1,len(playerCards)):
                    if playerCards[j].getValue() == playerCards[i].getValue():
                        playerHighCard = playerCards[i]
            for i in range(len(computerCards)):
                for j in range(i+1,len(computerCards)):
                    if computerCards[j].getValue() == computerCards[i].getValue():
                        computerHighCard = computerCards[i]

        elif score == "Two Pair":
            count = 1
            for i in range(len(playerCards)):
                for j in range(i+1,len(playerCards)):
                    if playerCards[j].getValue() == playerCards[i].getValue():
                        if count == 1:
                            firstPlayerCard = playerCards[i]
                            count = count + 1
                        elif count == 2:
                            secondPlayerCard = playerCards[i]
            count = 1
            for i in range(len(computerCards)):
                for j in range(i+1,len(computerCards)):
                    if computerCards[j].getValue() == computerCards[i].getValue():
                        if count == 1:
                            firstComputerCard = computerCards[i]
                            count = count + 1
                        elif count == 2:
                            secondComputerCard = computerCards[i]
            if min(int(firstPlayerCard.getValue()),
                   int(secondPlayerCard.getValue())) == 1:
                playerHighCard = max(int(firstPlayerCard.getValue()),
                                 int(secondPlayerCard.getValue()))
            else:                
                playerHighCard = max(int(firstPlayerCard.getValue()),
                                 int(secondPlayerCard.getValue()))
            if min(int(firstComputerCard.getValue()),
                   int(secondComputerCard.getValue())) == 1:
                computerHighCard = min(int(firstComputerCard.getValue()),
                                   int(secondComputerCard.getValue()))
            else:
                computerHighCard = max(int(firstComputerCard.getValue()),
                                   int(secondComputerCard.getValue()))

        elif score == "Three of a Kind":
            count = 0
            for i in range(len(playerCards)):
                for j in range(i+1,len(playerCards)):
                    if playerCards[j].getValue() == playerCards[i].getValue():
                        count = count + 1
                    if count == 2:
                        playerHighCard = playerCards[i]
                count = 0

            count = 0
            for i in range(len(computerCards)):
                for j in range(i+1,len(computerCards)):
                    if computerCards[j].getValue() == computerCards[i].getValue():
                        count = count + 1
                    if count == 2:
                        computerHighCard = computerCards[i]
                count = 0

        elif score == "Straight":
            ## Sort player and computer cards.
            for i in range(len(playerCards) - 1):
                flag = 0
                for j in range(len(playerCards) - 1):
                    if playerCards[j] > playerCards[j + 1]:
                        temp = playerCards[j]
                        playerCards[j] = playerCards[j + 1]
                        playerCards[j] = temp
                        flag = 1
                if flag == 0:
                    break
            for i in range(len(computerCards) - 1):
                flag = 0
                for j in range(len(computerCards) - 1):
                    if computerCards[j] > computerCards[j + 1]:
                        temp = computerCards[j]
                        computerCards[j] = computerCards[j + 1]
                        computerCards[j] = temp
                        flag = 1
                if flag == 0:
                    break
            
            count = 0
            for i in range(len(playerCards) - 1):
                card1 = int(playerCards[i].getValue())
                card2 = int(playerCards[i+1].getValue())
                if (card1 + 1) == card2:
                    count = count + 1
                elif (card1 + 1) != card2:
                    count = 0
                if count == 4:
                    playerHighCard = playerCards[i+1]

            count = 0
            for i in range(len(computerCards) - 1):
                card1 = int(computerCards[i].getValue())
                card2 = int(computerCards[i+1].getValue())
                if (card1 + 1) == card2:
                    count = count + 1
                elif (card1 + 1) != card2:
                    count = 0
                if count == 4:
                    computerHighCard = computerCards[i+1]

        #####################################
        #      NEEDS IMPLEMENTATION         #
        #####################################
        #elif score == "Flush":             #
        #elif score == "Full House":        #
        #elif score == "Four of a Kind":    #
        #elif score == "Straight Flush":    #
        #elif score == "Royal Flush":       #
        #####################################

        playerValue = playerHighCard.getValue()
        playerValue = int(playerValue)
        computerValue = computerHighCard.getValue()
        computerValue = int(computerValue)
        if playerValue == 1 and computerValue == 1:
            return "Tie"
        elif playerValue == 1:
            return "Player"
        elif computerValue == 1:
            return "Computer"
        elif playerValue > computerValue:
            return "Player"
        elif playerValue < computerValue:
            return "Computer"
        else:
            return "Tie"
        pass