import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("MrBalls123 Button Clicker")
wn.bgcolor("white")

click_count = 0

# Create turtles
pen = turtle.Turtle()
text_turtle = turtle.Turtle()

# Hide the text turtle and set up the pen
pen.hideturtle()
pen.penup()
pen.goto(-120, 220)
pen.write('Button Clicker:', align='left', font=('Arial', 16, 'normal'))
pen.goto(-85, 200)

# Draw the button
pen.goto(-100, 150)
pen.hideturtle()
pen.pendown()
pen.fillcolor("lightblue")
pen.begin_fill()
for _ in range(2):
    pen.forward(90)
    pen.left(90)
    pen.forward(30)
    pen.left(90)
pen.end_fill()
pen.penup()
pen.hideturtle()
pen.goto(-55, 155)
pen.write('CLICK ME!!!', align='center', font=('Arial', 10))

def update_text():
    global click_count
    click_count += 1
    text_turtle.clear()
    text_turtle.goto(-85, 190)  # Adjust position for the click count display
    text_turtle.write(f"Clicks: {click_count}", align='left', font=('Arial', 12, 'normal'))

def on_click(x, y):
    # Check if the click is within the button area
    if -55 < x < 35 and 150 < y < 180:  # Adjusted for button area
        update_text()

# Bind the click event to the on_click function
wn.onclick(on_click)

# Start the main loop
wn.mainloop()
