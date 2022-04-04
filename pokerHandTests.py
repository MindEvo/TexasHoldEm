##############################################################################
# Driver file for the PokerScorer Class
#
##############################################################################
def main():
    #Royal Flush Test
    p = ["11h", "10h"]
    houseCards = ["1h", "9h", "9s", "12h", "13h"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #Straight Flush Test
    p = ["11h", "10h"]
    houseCards = ["1d", "9h", "9s", "12h", "13h"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #Full House Test
    p = ["11h", "11d"]
    houseCards = ["11s", "9h", "9s", "12h", "13h"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #Flush Test
    p = ["2d", "11d"]
    houseCards = ["5d", "9h", "9d", "12d", "13h"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #Straight Test
    p = ["3s","5h"]
    houseCards = ["7d", "10s", "4c", "6s", "1d"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #3-of-a-Kind Test
    p = ["3s","5h"]
    houseCards = ["5d", "5s", "4c", "6s", "1d"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #Two Pair Test
    p = ["3s","5h"]
    houseCards = ["3d", "5s", "4c", "6s", "1d"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #One Pair Test
    p = ["4s","11h"]
    houseCards = ["3d", "5s", "4c", "6s", "1d"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
    #High Card Test
    p = ["1s","11h"]
    houseCards = ["3d", "5s", "4c", "6s", "12d"]
    print(p + houseCards)
    print(checkHand(p, houseCards))
    
##
#
def checkRoyalFlush(cardHand, houseCards):
    club = {"10c", "11c","12c","13c","1c"}
    diamond = {"10d", "11d","12d","13d","1d"}
    heart = {"10h", "11h","12h","13h","1h"}
    spade = {"10s", "11s","12s","13s","1s"}
    temp = set()
    temp.update(cardHand)
    temp.update(houseCards)
    return (club.issubset(temp) or diamond.issubset(temp) or heart.issubset(temp) or spade.issubset(temp))

##
#
def checkPair(cardHand, houseCards):
    temp = houseCards + cardHand
    temp.sort()
    temp = [i[ : -1] for i in temp]
    for i in range(len(temp)-1):
        if int(temp[i]) == int(temp[i + 1]):
            return True
        
    return False    
 
##
#   
def checkTwoPair(cardHand, houseCards):
    temp = houseCards + cardHand
    temp.sort()
    temp = [i[ : -1] for i in temp]
    pairCount = 0
    for i in range(len(temp)-1):
        if int(temp[i]) == int(temp[i + 1]):
            pairCount = pairCount + 1            
    if pairCount == 2:
        return True
    else:
        return False

##
#
def checkThreeOfAKind(cardHand, houseCards):
    temp = houseCards + cardHand
    temp.sort()
    temp = [i[ : -1] for i in temp]
    for i in range(len(temp)-2):
        if int(temp[i]) == int(temp[i + 1]) and int(temp[i + 1]) == int(temp[i + 2]):
            return True        
    return False

##
#
def checkStraight(cardHand, houseCards):
    temp = houseCards + cardHand
    temp = [i[ : -1] for i in temp]
    temp = list(map(int, temp))
    temp.sort()
    ## Check for A,K,Q,J,10 Straight
    #   If first card is an Ace, create a set with (10,J,Q,K), check if this
    #   is a subset of the temp.
    if temp[0] == 1:
        set1 = {10,11,12,13}
        set2 = set(temp)
        if set1.issubset(set2):
            return True
    ## Remove duplicates
    temp = set(temp)
    temp = list(temp)
    ## Count number of times (value + 1) equals next value in temp. If count
    #   reaches 4 return True. Reset count to zero whenever (value + 1) does
    #   not equal next value.
    count = 0
    for i in range(len(temp)-1):
        if temp[i] + 1 == temp[i+1]:
            count = count + 1
            if count == 4:
                return True
        else:
            count = 0
    return False

##
#
def checkFlush(cardHand, houseCards):
    temp = houseCards + cardHand
    suits = list()
    for i in range(len(temp)):
        x = temp[i]
        x = x[-1]
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

##
#
def checkFullHouse(cardHand, houseCards):
    if not checkThreeOfAKind(cardHand, houseCards):
        return False
    else:
        temp = houseCards + cardHand
        temp = [i[ : -1] for i in temp]
        temp = list(map(int, temp))
        temp = set(temp)
        if len(temp) == 4:
            return True
        else:
            return False

##
#
def checkStraightFlush(cardHand, houseCards):
    return checkFlush(cardHand, houseCards) and checkStraight(cardHand, houseCards)

##
#
def highCard(cardHand, houseCards):
    cards = cardHand + houseCards
    cards.sort()
    temp = [i[ : -1] for i in cards]
    temp = list(map(int, temp))
    largest = max(temp)
    smallest = min(temp)
    if smallest == 1:
        highCard = temp.index(smallest)
        result = "High Card: " + cards[highCard]
    else:
        highCard = temp.index(largest)
        result = "High Card: " + cards[highCard]
    return result
    

def checkHand(cardHand, houseCards):
    if checkRoyalFlush(cardHand, houseCards):
        return "Royal Flush"
    elif checkStraightFlush(cardHand, houseCards):
        return "Straight Flush"
    elif checkFullHouse(cardHand, houseCards):
        return "Full House"
    elif checkFlush(cardHand, houseCards):
        return "Flush"
    elif checkStraight(cardHand, houseCards):
        return "Straight"
    elif checkThreeOfAKind(cardHand, houseCards):
        return "3 of a Kind"
    elif checkTwoPair(cardHand, houseCards):
        return "Two Pair"
    elif checkPair(cardHand, houseCards):
        return "Pair"
    else:
        return highCard(cardHand, houseCards)

##############################################################################
main()