import turtle
t = turtle.Pen()
t.shape('turtle')

def DrawFlower():
    u = input("Can I draw you a flower? yes or no: ")
    if u == "yes":
        c = input("May I know your fav color? (red, orange, blue, green, purple): ")
        r = int(input("Please fill your radius (number): "))
        n = int(input("How many petal? (number): "))
        for i in range(n):
            t.pencolor(c)
            t.circle(r)
            t.rt(360/n)
    elif u == "no":
        print("No Problem")
    else:
        print("Invalid Reply")

DrawFlower()
