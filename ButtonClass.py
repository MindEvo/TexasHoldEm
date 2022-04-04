##############################################################################
# Button Class
#   Creates buttons for use with the pygame library.
##############################################################################
# Member variables
#   tuple of 3 ints type;   color
#   int type;               x
#   int type;               y
#   int type;               width
#   int type;               height
#   string type;            text
##############################################################################
import pygame

class Button():
###############
# CONSTRUCTOR #
###############    
    def __init__(self, color, x, y, width, height, text=''):
    ###########################################################################    
    # Initialize the button with parameters:
    #    Takes tuple of three ints between 0-255 for color.
    #    Takes integers for the x,y,width, and height parameters.
    #    Takes an optional string for the text compenent.
    ###########################################################################    
        self._color = color
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._text = text

############
# MUTATORS #
############
    def setColor(self, color):
        self._color = color
        
    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._height = height

    def setText(self, text):
        self._text = text

    def draw(self,win,outline=None):
    ###########################################################################    
    # Call this method to draw the button on the screen
    ###########################################################################    
        if outline:
            pygame.draw.rect(win, outline, 
                             (self._x-2, self._y-2, 
                              self._width+4 ,self._height + 4), 0)
            
        pygame.draw.rect(win, self._color, 
                         (self._x, self._y, self._width, self._height), 0)
        
        if self._text != '':
            font = pygame.font.SysFont('Times New Roman', 60)
            text = font.render(self._text, 1, (0,0,0))
            win.blit(text, (self._x + (self._width/2 - text.get_width()/2), 
                            self._y + (self._height/2 - text.get_height()/2)))
