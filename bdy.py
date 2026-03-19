import tkinter as tk
import random

width = 900
height = 600

root = tk.Tk()
root.title("Happy Birthday Bhawna Mam 🎉")

canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

colors = ["red","yellow","cyan","lime","orange","magenta","white"]

# balloons
balloons = []
for i in range(8):
    x = random.randint(50,850)
    y = random.randint(300,600)
    balloon = canvas.create_oval(x,y,x+40,y+50,fill=random.choice(colors))
    string = canvas.create_line(x+20,y+50,x+20,y+80,fill="white")
    balloons.append((balloon,string))

# confetti
confetti = []
for i in range(80):
    x = random.randint(0,width)
    y = random.randint(0,height)
    c = canvas.create_oval(x,y,x+4,y+4,fill=random.choice(colors),outline="")
    confetti.append(c)

# birthday text
text = canvas.create_text(
    width/2,80,
    text="🎉 HAPPY BIRTHDAY BHAWNA MAM 🎉",
    font=("Arial",36,"bold"),
    fill="white"
)

# fireworks particles
particles = []

def fireworks():
    x = random.randint(200,700)
    y = random.randint(100,300)

    for i in range(25):
        p = canvas.create_oval(x,y,x+5,y+5,fill=random.choice(colors),outline="")
        dx = random.randint(-6,6)
        dy = random.randint(-6,6)
        particles.append([p,dx,dy])

def animate():

    # balloons moving up
    for b,s in balloons:
        canvas.move(b,0,-2)
        canvas.move(s,0,-2)

        pos = canvas.coords(b)
        if pos[1] < -60:
            x = random.randint(50,850)
            canvas.coords(b,x,600,x+40,650)
            canvas.coords(s,x+20,650,x+20,680)

    # confetti falling
    for c in confetti:
        canvas.move(c,0,3)
        pos = canvas.coords(c)
        if pos[1] > height:
            x = random.randint(0,width)
            canvas.coords(c,x,0,x+4,4)

    # fireworks movement
    for p in particles:
        canvas.move(p[0],p[1],p[2])

    # change text color
    canvas.itemconfig(text, fill=random.choice(colors))

    # random fireworks
    if random.randint(1,15) == 1:
        fireworks()

    root.after(50, animate)

animate()

root.mainloop()