##############################################################################
# ImageSprite Class
#   Creates buttons for use with the pygame library. Inherits from the pygame
#   sprite class.
##############################################################################
# Member variables
#   int type;               x
#   int type;               y
#   string type;            filename
##############################################################################
import pygame

class ImageSprite(pygame.sprite.Sprite):
###############
# CONSTRUCTOR #
###############
   def __init__(self, x, y, filename) :
    ###########################################################################    
    # Parameters:
    #   x, y are ints for width and height.
    #   enter a string for the filename.
    ###########################################################################    
      super().__init__()
      self.loadImage(x, y, filename)

############
# MUTATORS #
############
   def loadImage(self, x, y, filename) :
    ###########################################################################    
    # Invokes the pygame rect method and places the image onto the rect.
    ###########################################################################    
      img = pygame.image.load(filename).convert()
      MAGENTA = (255, 0, 255)
      img.set_colorkey(MAGENTA)
      self.image = img
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y - self.rect.height
     
   def moveBy(self, dx, dy) :
    ###########################################################################    
    # Move the sprite a distance with respect to its current position.
    #   dx, dy are integers representing how far away on the x-y axis you want
    #   to move the sprite.
    ###########################################################################    
      self.rect.x += dx
      self.rect.y += dy
      
   def moveTo(self, x, y):
    ###########################################################################    
    # Move the sprite to a position on or off the screen.
    #   x and y are integers for the position you want to relocate the sprite.
    ###########################################################################    
       self.rect.x = x
       self.rect.y = y