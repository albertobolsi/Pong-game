
import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by Alberto")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
limit_score = 2
assert limit_score != 0
reached_limit = False



# Paddle A

paddle_A=turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

# Paddle B

paddle_B=turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

# Ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=-0.4
ball.dy=-0.4

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Game Over

game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("yellow")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)

# Play again?

play_again = ""
affirmative = ["Yes","yes","y","Y","Yep","yep"]
negative = ["No","no","n","N","Nope","nope"]
aff_answer = False
neg_answer = False


# Function

def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)



def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)






# Main Game loop

while neg_answer == False:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Keyboard inputs
    wn.listen()
    wn.onkeypress(paddle_A_up, "w")
    wn.onkeypress(paddle_A_down, "s")

    wn.onkeypress(paddle_B_up, "Up")
    wn.onkeypress(paddle_B_down, "Down")

    # Move the Ball

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Pong 2.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Pong 2.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Border checking

    if ball.xcor() > 330 and ball.xcor() <350 and (ball.ycor() < paddle_B.ycor() +59 and ball.ycor() > paddle_B.ycor() -59):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("Pong 2.wav", winsound.SND_ASYNC)


    if ball.xcor() < -330 and ball.xcor() > -350 and (ball.ycor() < paddle_A.ycor() + 59 and ball.ycor() > paddle_A.ycor() - 59):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("Pong 2.wav", winsound.SND_ASYNC)

    if score_a == limit_score or score_b == limit_score:
        winsound.PlaySound("game over.wav", winsound.SND_ASYNC)
        game_over.write("GAME OVER", align="center", font=("Verdana", 40, "normal"))
        play_again = wn.textinput("Game Over", "Play again?")
        aff_answer = any(element in play_again for element in affirmative)
        neg_answer = any(element in play_again for element in negative)
        if aff_answer == True:
            score_a = 0
            score_b = 0
            game_over.clear()
            pen.clear()
            pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))



















