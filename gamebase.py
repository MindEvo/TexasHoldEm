# This file contains the Poker class which handles most of the funtionality of
#   the game. 
#
###############################################################################
###############################################################################
import ButtonClass as BC
import PersonClass as Person
import DeckClass as Deck
import PokerScorerClass as PSC
import ImageSpriteClass as ISC
import pygame


class Poker:
    ante = 100
    def __init__(self, width, height):
        ######################
        ## Pygame Variables ##
        ######################
        pygame.init()
        self._width = width
        self._height = height
        self._display = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Texas Hold 'Em")
        self._clock = pygame.time.Clock()
        self._framesPerSecond = 30
        self._sprites = pygame.sprite.LayeredUpdates()
        self._ticks = 0
        pygame.key.set_repeat(1, 120)
        ######################
        ## Poker Variables  ##
        ######################
        self.scorer = PSC.PokerScorer()
        self._deck = Deck.Deck()
        self._theHouse = Person.Person("House", 0)
        self._Player = Person.Person("Player", 5000)
        self._Computer = Person.Person("Computer", 5000)
        self._flopDealt = False
        self._turnDealt = False
        self._riverDealt = False
        self._gameOver = False
        self._winner = ""
        ##############################
        ## Button and Msg Variables ##
        ##############################
        self.WinMsg = BC.Button((125,125,125), 3000, 3000, 800, 75,'')
        self.NextGmBtn = BC.Button((125,0,0), 3000,3000, 300, 100,"Next Game")
        self.CheckButton = BC.Button((125,125,125), 1075, 300, 160, 65,"Check")
        self.FoldButton = BC.Button((125,125,125), 1075, 400, 160, 65,"Fold")
        self.RaiseButton = BC.Button((125,125,125), 1075, 200, 160, 65,"Raise")
        self.RaiseMore = BC.Button((125,125,125), 2000, 2000, 75, 85, "↑")
        self.RaiseLess = BC.Button((125,125,125), 2000, 2000, 75, 85,"↓")
        self.RaiseAmount = 100
        self.RaiseDisplay = BC.Button((125,125,125), 2000, 2000, 175, 75, str(self.RaiseAmount))
        self.RaiseConfirm = BC.Button((125,125,125), 2000,2000, 275, 50, "CONFIRM")
        self.EndGame = BC.Button((125,125,125),2000,2000,500,500,"")

##############################################################################
#                           Pygame Methods                                   #
##############################################################################
##############################################################################
    def mouseButtonDown(self, x, y):
        return

    def keyDown(self, key) :
        return

    def update(self):
        self._sprites.update()

    def draw(self):
        self._sprites.draw(self._display)

    def add(self, sprite):
        self._sprites.add(sprite)

    def getTicks(self):
        return self._ticks

    def quit(self):
        pygame.quit()

    def drawBackground(self):
    ###########################################################################    
    # Create the display background graphics
    ###########################################################################    
        background = ISC.ImageSprite(100, 100, 
                                 "D:/CompSci/Projects/Python Poker/table.gif")
        background.moveBy(-60, 600)
        self.add(background)
        
    def drawInfo(self):
    ###########################################################################    
    # Display the pot, ante, player wallet, and dealer bank.
    ###########################################################################    
        font = pygame.font.SysFont("Times New Roman", 30)
        potAmount = font.render("Pot:   $" + 
                                str(self._theHouse.getMoney()), 
                                True, (255,255,255))
        ante = font.render("Ante: $100", True, (255,255,255))
        playerAmount = font.render("Player Wallet: $" + 
                                   str(self._Player.getMoney()), 
                                   True, (255,255,255))
        dealerAmount = font.render("Computer Bank: $" + 
                                   str(self._Computer.getMoney()), 
                                   True, (255,255,255))
        self._display.blit(potAmount, (50,300))
        self._display.blit(ante, (50, 335))
        self._display.blit(dealerAmount, (50, 25))
        self._display.blit(playerAmount, (50, 660))

##############################################################################
#                           Game Logic Methods                               #
#                                                                            #
##############################################################################       
    def clearTable(self):
    ###########################################################################    
    ## Removes all the cards from the table.
    ###########################################################################    
        self._Player.removeCards()
        self._Computer.removeCards()
        self._theHouse.removeCards()
        ## Move the winner display and next game button off the display.
        #
        self.WinMsg.setX(3000)
        self.WinMsg.setY(3000)
        self.NextGmBtn.setX(3000)
        self.NextGmBtn.setX(3000)
        ## Reset the gameOver and winner variables for the next game.
        #
        self._flopDealt = False
        self._turnDealt = False
        self._riverDealt = False
        self.gameOver = False
        self._winner = ""

    def newRound(self):
    ###########################################################################    
    # Deal cards to the player, compuer, and place the ante.
    ###########################################################################    
        self._deck.shuffleDeck()
        #################################
        ## Deal the player's two cards ##
        #################################
        self._Player.addCard(self._deck.drawCard())
        self.add(self._Player.getCard(0).getSprite())
        self._Player.getCard(0).moveCard(500,595)
        self._Player.addCard(self._deck.drawCard())
        self.add(self._Player.getCard(1).getSprite())
        self._Player.getCard(1).moveCard(600,595)
        ###################################
        ## Deal the Computer's two cards ##
        ###################################
        self._Computer.addCard(self._deck.drawCard())
        self._Computer.hideCard(0)
        self.add(self._Computer.getCard(0).getSprite())
        self._Computer.getCard(0).moveCard(500,25)
        self._Computer.addCard(self._deck.drawCard())
        self._Computer.hideCard(1)
        self.add(self._Computer.getCard(1).getSprite())
        self._Computer.getCard(1).moveCard(600,25)
        ####################
        ## Place the ante ##
        ####################
        self._Player.removeMoney(100)
        self._Computer.removeMoney(100)
        self._theHouse.addMoney(200)

    def flop(self):
    ###########################################################################    
    # Draw three cards for the house and place in the middle of the table.
    ###########################################################################    
        self._flopDealt = True
        self._theHouse.addCard(self._deck.drawCard())
        self.add(self._theHouse.getCard(0).getSprite())
        self._theHouse.getCard(0).moveCard(400,300)
        self._theHouse.addCard(self._deck.drawCard())
        self.add(self._theHouse.getCard(1).getSprite())
        self._theHouse.getCard(1).moveCard(500,300)
        self._theHouse.addCard(self._deck.drawCard())
        self.add(self._theHouse.getCard(2).getSprite())
        self._theHouse.getCard(2).moveCard(600,300)

    def theTurn(self):
    ###########################################################################    
    # Draw fourth card for the house and place into the middle of the table.
    ###########################################################################    
        self._turnDealt = True
        self._theHouse.addCard(self._deck.drawCard())
        self.add(self._theHouse.getCard(3).getSprite())
        self._theHouse.getCard(3).moveCard(700,300)

    def theRiver(self):
    ###########################################################################    
    # Draw fifth card for the house and place into the middle of the table.
    ###########################################################################    
        self._riverDealt = True
        self._theHouse.addCard(self._deck.drawCard())
        self.add(self._theHouse.getCard(4).getSprite())
        self._theHouse.getCard(4).moveCard(800,300)
##############################################################################
#                           GamePlay Methods                                 #
#                                                                            #
##############################################################################
    def showRaiseMenu(self):
    ###########################################################################    
    # Display the buttons for raising and amount to raise by.
    ###########################################################################    
        self.RaiseMore.setX(850)
        self.RaiseMore.setY(25)
        self.RaiseDisplay.setX(950)
        self.RaiseDisplay.setY(25)
        self.RaiseLess.setX(1150)
        self.RaiseLess.setY(25)
        self.RaiseConfirm.setX(905)
        self.RaiseConfirm.setY(115)
    
    def hideRaiseMenu(self):
    ###########################################################################    
    # Hide the buttons for raising.
    ###########################################################################    
        self.RaiseMore.setX(2000)
        self.RaiseMore.setY(2000)
        self.RaiseDisplay.setX(2000)
        self.RaiseDisplay.setY(2000)
        self.RaiseLess.setX(2000)
        self.RaiseLess.setY(2000)
        self.RaiseConfirm.setX(2000)
        self.RaiseConfirm.setY(2000)
                
    def confirmRaise(self,level,amount):
    ###########################################################################    
    # Raise the bet by the amount passed through.
    #   Call either flop, turn, or river based on level passed in.
    ###########################################################################    
        self.hideRaiseMenu()
        self.RaiseAmount = 100
        self.RaiseDisplay.setText(str(self.RaiseAmount))
        self._Player.removeMoney(amount)
        self._Computer.removeMoney(amount)
        self._theHouse.addMoney(2 * amount)
        if level == 0:
            self.flop()
        if level == 1:
            self.theTurn()
        if level == 2:
            self.theRiver()
        pass

    def check(self, level):
    ###########################################################################    
    # Player can continue without placing any bets.
    ###########################################################################    
        if level == 0:
            self.flop()
        if level == 1:
            self.theTurn()
        if level == 2:
            self.theRiver()
        self.hideRaiseMenu()
    
    def fold(self):
    ###########################################################################    
    # Player gives up their hand and loses the pot.
    ###########################################################################    
        self._gameOver = True
        self._winner = "Computer"
        self._Computer.showCard(0)
        self.add(self._Computer.getCard(0).getSprite())
        self._Computer.getCard(0).moveCard(500,25)
        self._Computer.showCard(1)
        self.add(self._Computer.getCard(1).getSprite())
        self._Computer.getCard(1).moveCard(600,25)
        self.updatePot()
        self.hideRaiseMenu()

##############################################################################
#                      Win Condition Methods                                 #
#                                                                            #
##############################################################################
    def checkHand(self, cardHand):
    ###########################################################################    
    # Look through cards to see if a poker hand was made.
    #   Returns a string of the hand found.
    ###########################################################################    
        if self.scorer.royalFlush(cardHand, self._theHouse.getHand()):
            return "Royal Flush"
        elif self.scorer.straightFlush(cardHand, self._theHouse.getHand()):
            return "Straight Flush"
        elif self.scorer.fourOfAKind(cardHand, self._theHouse.getHand()):
            return "Four of a Kind"
        elif self.scorer.fullHouse(cardHand, self._theHouse.getHand()):
            return "Full House"
        elif self.scorer.flush(cardHand, self._theHouse.getHand()):
            return "Flush"
        elif self.scorer.straight(cardHand, self._theHouse.getHand()):
            return "Straight"
        elif self.scorer.threeOfAKind(cardHand, self._theHouse.getHand()):
            return "Three of a Kind"
        elif self.scorer.twoPair(cardHand, self._theHouse.getHand()):
            return "Two Pair"
        elif self.scorer.pair(cardHand, self._theHouse.getHand()):
            return "Pair"
        else:
            return "High Card"

    def checkWinner(self):
    ###########################################################################
    # Use to compare hands between the player and the computer to see who
    #   won the round. Call the checkHand method on player and computer to get
    #   their hand. Index them in the scores list, lowest index has the best
    #   hand and is winner.
    ###########################################################################
        scores = ["Royal Flush", "Straight Flush", "Four of a Kind", 
                  "Full House", "Flush", "Straight", "Three of a Kind", 
                  "Two Pair", "Pair", "High Card"]
        playerScore = self.checkHand(self._Player.getHand())
        computerScore = self.checkHand(self._Computer.getHand())
        for i in range(len(scores)):
            if playerScore == scores[i]:
                pIndex = i
            if computerScore == scores[i]:
                cIndex = i
        if pIndex < cIndex:
            self._winner = "Player"
            return "Player Wins: " + scores[pIndex]
        elif cIndex < pIndex:
            self._winner = "Computer"
            return "Computer Wins: " + scores[cIndex]
        elif pIndex == cIndex:
            self._winner == "Tie"
            return "Tie"
        #####################################################################
        ## Tiebreaker code not complete.
        #####################################################################
        #   self._winner = self.scorer.tieBreaker(playerScore, 
        #                                         self._Player.getHand(),
        #                                         self._Computer.getHand(),
        #                                         self._theHouse.getHand())
        #   if self._winner == "Tie":
        #       return "Tie"
        #   elif self._winner == "Player":
        #       return "Player Wins: " + scores[pIndex]
        #   elif self._winner == "Computer":
        #       return "Computer Wins:" + scores[cIndex]
        #####################################################################

    def updatePot(self):
    ###########################################################################    
    #   Pays out the pot to the winner.
    ###########################################################################    
        if self._winner == "Tie":
            self._Player.addMoney(self._theHouse.getMoney() / 2)
            self._Computer.addMoney(self._theHouse.getMoney() / 2)
            self._theHouse.removeMoney(self._theHouse.getMoney())
        elif self._winner == "Computer":
            self._Computer.addMoney(self._theHouse.getMoney())
            self._theHouse.removeMoney(self._theHouse.getMoney())
        elif self._winner == "Player":
            self._Player.addMoney(self._theHouse.getMoney())
            self._theHouse.removeMoney(self._theHouse.getMoney())


    def run(self):
    ###########################################################################    
    # Runs the game by executing the game and event loops.
    #   Uses a counter variable named level to keep track of flop turn and
    #   river.
    #       0 == Flop
    #       1 == Turn
    #       2 == River
    #   Calls the drawBackground and newRound methods.
    ###########################################################################    
        level = 0
        self.drawBackground()
        self.newRound()
        #######################################################################
        #                       Game Loop                                     #
        #---------------------------------------------------------------------#
        #   Stores the mouse position, runs the event loop and updates the    #
        #   display.                                                          #
        #######################################################################
        while True:
            mx, my = pygame.mouse.get_pos()
            ###################################################################
            #                       Event Loop                                #
            #-----------------------------------------------------------------#
            #                                                                 #
            ###################################################################
            for event in pygame.event.get():
                ###############################################################
                ## At level 4, all cards have been dealt and final bets made.
                #   -Show computers cards
                #   -Display message with winner and hand
                #   -Display next game button
                ###############################################################
                if level == 4:
                    self._gameOver = True
                    self._Computer.showCard(0)
                    self.add(self._Computer.getCard(0).getSprite())
                    self._Computer.getCard(0).moveCard(500,25)
                    self._Computer.showCard(1)
                    self.add(self._Computer.getCard(1).getSprite())
                    self._Computer.getCard(1).moveCard(600,25)
                    text = self.checkWinner()
                    self.updatePot()
                    self.WinMsg.setText(text)
                    self.WinMsg.setX(240)
                    self.WinMsg.setY(450)
                    self.NextGmBtn.setX(940)
                    self.NextGmBtn.setY(600)

                if event.type == pygame.QUIT:
                    self.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN :
                    ###########################################################
                    ## Click on Raise
                    ###########################################################
                    self.mouseButtonDown(event.pos[0], event.pos[1])
                    if (mx > 1075 and mx < 1175) and (my > 200 and my < 250):
                        self.showRaiseMenu()
                    if self.RaiseConfirm._x == 905:
                        if (mx > 850 and mx < 925) and (my >25 and my < 110):
                            if (self.RaiseAmount + 100 < self._Player.getMoney() 
                                and
                                self.RaiseAmount + 100 < self._Computer.getMoney()
                                ):
                                self.RaiseAmount = self.RaiseAmount + 100
                                self.RaiseDisplay.setText(str(self.RaiseAmount))
                        if (mx > 1150 and mx < 1250) and (my >25 and my < 110):
                            if (self.RaiseAmount - 100 > 0):
                                self.RaiseAmount = self.RaiseAmount - 100
                                self.RaiseDisplay.setText(str(self.RaiseAmount))
                        if (mx > 905 and mx < 1180) and (my > 115 and my < 165):
                            self.confirmRaise(level, self.RaiseAmount)
                            level = level + 1
                    ###########################################################
                    ## Click on Check
                    ###########################################################
                    if (mx > 1075 and mx < 1175) and (my > 300 and my < 350):
                        self.check(level)
                        level = level + 1
                    ###########################################################
                    ## Click on Fold
                    ###########################################################
                    if (mx > 1075 and mx < 1175) and (my > 400 and my < 450):
                        level = 0
                        self.fold()
                        self.clearTable()
                        self.newRound()
                    ###########################################################
                    ## Click on Next Game
                    ###########################################################
                    if (mx > 940 and mx < 1280) and (my > 600 and my < 720):
                        if self._gameOver == True:
                            self.clearTable()
                            self.newRound()
                            level = 0
                        
                elif event.type == pygame.KEYDOWN :
                    self.keyDown(event.key)
                    ###########################################################
                    ## Future Keyboard Support Here
                    ###########################################################
                    
                ###############################################################
                #                       Display Updates                       #
                #                                                             #
                ###############################################################                
                self.update()
                self.draw()
                self.drawInfo()
                self.RaiseButton.draw(self._display)
                self.CheckButton.draw(self._display)
                self.FoldButton.draw(self._display)
                self.RaiseMore.draw(self._display)
                self.RaiseLess.draw(self._display)
                self.RaiseDisplay.draw(self._display)
                self.RaiseConfirm.draw(self._display)
                self.WinMsg.draw(self._display)
                self.NextGmBtn.draw(self._display)
                pygame.display.update()
                self._clock.tick(self._framesPerSecond)
                self._ticks += 1
