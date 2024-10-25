from tkinter import *
import time

mario = []
state = 0
x = 2   #minha raiz da equação
wpressed = False
walking = False
animationJump = False
def keyA(event):
    global state, walking, wpressed
    if not (wpressed):
        state = 3
        canva.itemconfig(elemento, image=mario[4])
        if not(walking): window.after(500, lambda: canva.itemconfig(elemento, image=mario[state]))
    canva.move(elemento, -5, 0)
    window.update()
    time.sleep(0.01)
    canva.move(elemento, -5, 0)
    window.update()
def keyE(event):
    keyW(1)
def keyQ(event):
    keyW(0)
def keyW(event):
    global state, wpressed
    if state == 0: state = 2
    if state == 3: state = 5
    if wpressed == False:    # ISTO AQUI FOI O DIFICIL
       wpressed = True
       canva.itemconfig(elemento, image=mario[state])
       for x in range (-40,41):
            raiz = -2*x  #derivada
            raiz = -raiz #porque numeros positivos representam para baixo no Canvas, e deve ser o inverso

            if event == 1:
                canva.move(elemento, 3, raiz / 8)
            elif event == 0:
                canva.move(elemento, -3, raiz / 8)
            else:
                canva.move(elemento, 0, raiz / 8)
            time.sleep(0.01)      #speed of the jump / framerate of the jump
            window.update()

       wpressed = False
       window.after(int(0.01*80) , lambda: canva.itemconfig(elemento, image=mario[state-2]))

keyEsc = lambda event:window.quit()

def keyD(event):
    global state
    global wpressed
    global walking
    if not(wpressed):
        state = 0
        canva.itemconfig(elemento, image=mario[1])
        if not(walking): window.after(500, lambda: canva.itemconfig(elemento, image=mario[state]))
    canva.move(elemento, 10, 0)
    window.update()




window = Tk()

canva = Canvas(window,width=853,height=480)
canva.pack()

background = PhotoImage(file='Cn0Nooe.png')
canva.create_image(0,0, image=background, anchor=NW)
mario.append(PhotoImage(file='mario-default.png').subsample(4,4))
mario.append(PhotoImage(file='mario-walking.png').subsample(4,4))
mario.append(PhotoImage(file='mario-jumping.png').subsample(4,4))
mario.append(PhotoImage(file='mario-default1.png').subsample(4,4))
mario.append(PhotoImage(file='mario-walking1.png').subsample(4,4))
mario.append(PhotoImage(file='mario-jumping1.png').subsample(4,4))

elemento = canva.create_image(100, 365, image=mario[state], anchor=CENTER)
coordenadas = canva.coords(elemento)

window.bind('<a>',keyA)
window.bind('<w>',keyW)
window.bind('<d>',keyD)
window.bind('<e>',keyE)
window.bind('<q>',keyQ)
window.bind('<Escape>',keyEsc)

footer = Label(window,text="2024 Made by Pepe 👌",font=("Courier New",10),bg="#CCCCCC",bd=4,relief=RIDGE,padx=10,anchor="w")
footer.pack(fill = "x", expand = True,side=BOTTOM)

window.mainloop()