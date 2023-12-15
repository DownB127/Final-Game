# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:33:06 2023

@author: Down.B
"""

"""adventure game with inventory"""
import pygame, simpleGE

class Node(object):
    def __init__(self, title, desc, aText, aIndex, bText, bIndex):
        self.title = title
        self.description = desc
        self.aText = aText
        self.aIndex = aIndex
        self.bText = bText
        self.bIndex = bIndex

class GameScreen(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
       
        self.lblTitle = simpleGE.Label()
        self.lblTitle.font = pygame.font.Font("C:\Windows\Fonts\Forte.ttf",50)
        self.lblTitle.center = (320, 35)
        self.lblTitle.size = (550, 60)
        
        self.lblDescription = simpleGE.MultiLabel()
        self.lblDescription.font = pygame.font.Font("goodfoot.ttf", 30)
        self.lblDescription.bgColor = (0x0, 0xFF, 0xFF)
        self.lblDescription.center = (320,240)
        self.lblDescription.size = (550, 320)
        
        self.btnA = simpleGE.Button()
        self.btnA.bgColor = (0xE0, 0xFF, 0xFF)
        self.btnA.font = pygame.font.Font("goodfoot.ttf", 30)
        self.btnA.center = (150, 420)
        self.btnA.size = (250, 40)
        
        self.btnB = simpleGE.Button()
        self.btnB.bgColor = (0xE0, 0xFF, 0xFF)
        self.btnB.font = pygame.font.Font("goodfoot.ttf", 30)
        self.btnB.center = (490, 420)
        self.btnB.size = (250, 40)
        
        self.sprites = [self.lblTitle, self.lblDescription, 
                        self.btnA, self.btnB]
                        
        self.background.fill((0x0, 0xFF, 0xFF))
        
        self.item = False
        
    def loadNode(self, node):
        self.lblTitle.text = node.title
        self.lblDescription.textLines = node.description
        self.btnA.text = node.aText
        self.btnB.text = node.bText
        self.aIndex = node.aIndex
        self.bIndex = node.bIndex
        
    def update(self):
        if self.btnA.clicked:
            if self.aIndex == -1:
                self.keepGoing = False
            if self.aIndex == 1:
                self.item = True
            if self.aIndex == 3:
                if self.item == True:
                    self.loadNode(self.nodeList[3])
                else:
                    self.loadNode(self.nodeList[4])
            if self.aIndex == 9:
                if self.item == True:
                    self.loadNode(self.nodeList[self.aIndex])
                else:
                    self.loadNode(self.nodeList[10])
            else:
                self.loadNode(self.nodeList[self.aIndex])
    
        if self.btnB.clicked:
            if self.bIndex == -1:
                self.keepGoing = False
            else:
                self.loadNode(self.nodeList[self.bIndex])
            
    """when user gets an item, take them to a separate screen to lead them back on the main path"""
    """use if, else statements to judge whether there is an item"""
    
def main():
    
    nodeList = []
    
    #0
    nodeList.append(Node(
        "Dark Room",
        [    "You wake up in a dimly lit room",
             "Without much idea as to where you are",
             "However, there are two doors in front",
             "of you, one to your left and right.",
             "Which should you enter?"
             
        ],
        "Left door", 1,
        "Right door", 2
        ))
  
    #1
    nodeList.append(Node(
        "You picked up the key!",
        [   "You can use this later",
             "If you want to",
        ],
        "Move forward", 2,
        "Move forward", 2
        ))
    
    #2
    nodeList.append(Node(
        "Split paths",
        [   "In front of you, you see a large door",
            "With a small keyhole to its side.",
            "To its left, you see a smaller, less",
            "Impressive door",
        ],
        "Try the locked door", 3,
        "Try the smaller door", 4
        ))
    
    #3
    nodeList.append(Node(
        "Large door",
        [   "After unlocking the door, you see",
             "A large room in front of you, filled",
             "With dangerous objects. You see a door",
             "Near the end, with a winding path to your left",
        ],
        "Walk through", 11,
        "Go around", 12
        ))
    
    #4
    nodeList.append(Node(
        "Small door",
        [   "Detered by the lack of a key, you open",
            "The smaller door, and see a tightrope",
            "Across a large gap. You could test your balance,",
            "or try and grab the rope from below.",
        ],
        "Walk on top", 5,
        "Grab from below", 6
        ))
    
    #5
    nodeList.append(Node(
        "Tightrope walk",
        [   "You attempt to walk the tightrope, but",
             "without proper balance, you quickly fall",
             "into the chasm below",
        ],
        "Start over", 0,
        "Quit", -1
        ))
    
    #6
    nodeList.append(Node(
        "Starcase",
        [   "At the end of the rope you find",
            "a spiral staircase leading both",
            "upwards and downwards"
        ],
        "Go upstairs", 8,
        "Go downstairs",7
        ))
    
    #7
    nodeList.append(Node(
        "Downstairs",
        [   "These stairs seem to",
             "Simply go down forever..."
        ],
        "Go upstairs", 8,
        "Go downstairs", 7
        ))
    
    #8
    nodeList.append(Node(
        "Upstairs",
        [   "Finally at the top of the stairs, you see",
            "a final set of doors, one locked, the other",
            "is swung wide open",
            "Which will you go through?"
        ],
        "Locked door", 9,
        "Open door", 10
        ))
    
    #9
    nodeList.append(Node(
        "ENDING 1",
        [   "Using your key that you had saved, you open",
             "the final door, only to reveal mountains",
             "of gold and valuables",
             "You Win!"
        ],
        "Play again", 0,
        "Quit", -1
        ))
    
    #10
    nodeList.append(Node(
        "ENDING 2",
        [   "Lacking a proper key to use, you simply",
             "enter the open door, only to reveal a way",
             "out into the light. You win, although you",
             "feel as if you've missed something",
        ],
        "Play again", 0,
        "Quit", -1
        ))
    
    #11
    nodeList.append(Node(
        "Run through",
        [   "You attempt to dash through all of the",
             "traps laid out before you, but the traps",
             "do their job, and quickly render you immobile",
        ],
        "Play again", 0,
        "Quit", -1
        ))
    
    #12
    nodeList.append(Node(
        "Long route",
        [   "Despite taking a while, you",
            "make it through in one piece.",
            "Now, you're faced with a simple decision, ",
            "Left or right?",
        ],
        "Left", 13,
        "Right", 14
        ))
    
    #13
    nodeList.append(Node(
        "ENDING 3",
        [   "You finally make it outside, albiet",
             "a little worse for wear. You decide to",
             "forget that this happened, and move on.",     
        ],
        "Play again", 0,
        "Quit", -1
        ))
    
    #14
    nodeList.append(Node(
        "ENDING 4",
        [   "You go down the right hallway, only to see",
            "A paper lying on the table. It reads:",
            "Use the key with the small door.",
            "It seems you've overlooked something, but,",
            "You still win!"
        ],
        "Play again", 0,
        "Quit", -1
        ))
    
        
    
    nodeList.append(Node(
        "",
        [   "",
            "",
            "",
            "",
            "",
            "",
            "",
        ],
        "", 0,
        "", 0))
    
    
    game = GameScreen()
    game.nodeList = nodeList
    game.loadNode(nodeList[0])
    game.setCaption("Island Adventure")
    game.start()
    
if __name__ == "__main__":
    main()
        
        
        
        
        
        