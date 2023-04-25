from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('Blackjack Game')
root.geometry("1000x800")
root.configure(background="gray")

#resize images of cards
def resize(card):
    img = Image.open(card)

    #resize
    newImg = img.resize((150,218))
    global returnImg
    returnImg = ImageTk.PhotoImage(newImg)
    return returnImg

newFrame = Frame(root, background="gray")
newFrame.pack(pady=20)
#Frames for cards
dealerFrame = LabelFrame(newFrame,text="Dealer", border=0)
dealerFrame.pack(ipadx=20,pady=10)
playerFrame = LabelFrame(newFrame,text="Player",border=0)
playerFrame.pack(ipadx=20,pady=10)




#dealer frames for cards
dLabel_1 = Label(dealerFrame, text='')
dLabel_1.grid(row = 0, column = 0, padx=20,pady=20)

dLabel_2 = Label(dealerFrame, text='')
dLabel_2.grid(row = 0, column = 1, padx=20,pady=20)

dLabel_3 = Label(dealerFrame, text='')
dLabel_3.grid(row = 0, column = 2, padx=20,pady=20)

dLabel_4 = Label(dealerFrame, text='')
dLabel_4.grid(row = 0, column = 3, padx=20,pady=20)

dLabel_5 = Label(dealerFrame, text='')
dLabel_5.grid(row = 0, column = 4, padx=20,pady=20)


#player frames for cards
pLabel_1 = Label(playerFrame, text='')
pLabel_1.grid(row = 1, column = 0,padx=20,pady=20)

pLabel_2 = Label(playerFrame, text='')
pLabel_2.grid(row = 1, column = 1,padx=20,pady=20)

pLabel_3 = Label(playerFrame, text='')
pLabel_3.grid(row = 1, column = 2,padx=20,pady=20)

pLabel_4 = Label(playerFrame, text='')
pLabel_4.grid(row = 1, column = 3,padx=20,pady=20)

pLabel_5 = Label(playerFrame, text='')
pLabel_5.grid(row = 1, column = 4,padx=20,pady=20)

def resetDeck():
    #Clear previous cards
    pLabel_1.config(image='')
    pLabel_2.config(image='')
    pLabel_3.config(image='')
    pLabel_4.config(image='')
    pLabel_5.config(image='')

    dLabel_1.config(image='')
    dLabel_2.config(image='')
    dLabel_3.config(image='')
    dLabel_4.config(image='')
    dLabel_5.config(image='')
    #Create Deck
    suits = ["spades","clubs","hearts","diamonds"]
    values = range(2,15)
    global deck
    deck = []

    #fill deck
    for x in suits:
        for y in values:
            deck.append(f'{y}_of_{x}')

    #Create Players
    global dealerHand,playerHand
    playerHand = []
    dealerHand = []
    global dSpot, pSpot
    dSpot = 0
    pSpot = 0

    #deal cards
    playerHit()
    dealerHit()

    
def playerHit():
    if pSpot < 5:
        #deal to player
        card = random.choice(deck)
        playerHand.append(card)
        deck.remove(card)
        #place card into frame
        global pImage
        pImage = resize(fr'C:\Users\Evan\Desktop\BlackJack_Project\PNG-cards-1.3\{card}.png')
        pLabel_1.config(image = pImage)
        

def dealerHit():
    if dSpot < 5:
        #deal to dealer
        card = random.choice(deck)
        dealerHand.append(card)
        deck.remove(card)
        #place card into frame
        global dImage
        dImage = resize(fr'C:\Users\Evan\Desktop\BlackJack_Project\PNG-cards-1.3\{card}.png')
        dLabel_1.config(image = dImage)



buttonFrame = Frame(root, background="gray")
buttonFrame.pack(pady=20)
#Create buttons to manipulate cards
hitButton = Button(buttonFrame, text="HIT")
hitButton.grid(row= 0, column = 1,padx=5,pady=5)

standButton = Button(buttonFrame, text="STAND")
standButton.grid(row= 0, column = 2,padx=5,pady=5)

doubleButton = Button(buttonFrame, text="DOUBLE")
doubleButton.grid(row= 1, column = 1,padx=5,pady=5)

splitButton = Button(buttonFrame, text="SPLIT")
splitButton.grid(row= 1, column = 2,padx=5,pady=5)

resetGame = Button(buttonFrame, text="RESET GAME",command=resetDeck())
resetGame.grid(row= 0, column = 0,padx=5,pady=5,)





root.mainloop() 