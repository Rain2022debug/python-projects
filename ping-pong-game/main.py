import turtle
import random

# Paddle class
class Paddle:
    def __init__(self, x_pos):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_pos, 0)

    def move_up(self):
        y = self.paddle.ycor()
        if y < 250:  # Boundary check
            y += 20
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        if y > -240:  # Boundary check
            y -= 20
        self.paddle.sety(y)

# Ball class
class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(1)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2.5  # Ball's initial speed in x direction
        self.ball.dy = 2.5  # Ball's initial speed in y direction

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def bounce_y(self):
        self.ball.dy *= -1

    def bounce_x(self):
        self.ball.dx *= -1.2  # Speed up the ball

    def reset_position(self):
        self.ball.goto(0, 0)
        self.ball.dx = random.choice([1.5, 3.5]) if self.ball.dx < 0 else random.choice([-3.5, -1.5])
        self.ball.dy = random.choice([1.5, 3.5]) if self.ball.dy < 0 else random.choice([-3.5, -1.5])

# ScoreBoard class
class ScoreBoard:
    def __init__(self):
        self.score_a = 0
        self.score_b = 0
        self.display = turtle.Turtle()
        self.display.speed(0)
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.display.clear()
        self.display.write(f"Player A: {self.score_a}  Player B: {self.score_b}",
                           align="center", font=("Courier", 24, "normal"))

    def increase_score_a(self):
        self.score_a += 1
        self.update_score()

    def increase_score_b(self):
        self.score_b += 1
        self.update_score()

# PongGame class
class PongGame:
    def __init__(self):
        self.setup_screen()
        self.paddle_a = Paddle(-350)
        self.paddle_b = Paddle(350)
        self.ball = Ball()
        self.scoreboard = ScoreBoard()
        self.draw_middle_line()
        self.bind_keys()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

    def draw_middle_line(self):
        line = turtle.Turtle()
        line.speed(0)
        line.color("white")
        line.penup()
        line.hideturtle()
        line.goto(0, -300)
        line.pendown()
        line.setheading(90)
        for _ in range(15):
            line.forward(20)
            line.penup()
            line.forward(20)
            line.pendown()

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkeypress(self.paddle_a.move_up, "w")
        self.screen.onkeypress(self.paddle_a.move_down, "s")
        self.screen.onkeypress(self.paddle_b.move_up, "Up")
        self.screen.onkeypress(self.paddle_b.move_down, "Down")

    def check_collisions(self):
        # Ball and wall collisions
        if self.ball.ball.ycor() > 290 or self.ball.ball.ycor() < -290:
            self.ball.bounce_y()

        # Ball and paddle collisions
        if (self.ball.ball.xcor() > 340 and self.ball.ball.distance(self.paddle_b.paddle) < 50) or \
           (self.ball.ball.xcor() < -340 and self.ball.ball.distance(self.paddle_a.paddle) < 50):
            self.ball.bounce_x()

        # Ball out of bounds
        if self.ball.ball.xcor() > 390:
            self.scoreboard.increase_score_a()
            self.ball.reset_position()
        elif self.ball.ball.xcor() < -390:
            self.scoreboard.increase_score_b()
            self.ball.reset_position()

    def run(self):
        while True:
            try:
                self.screen.update()
                self.ball.move()
                self.check_collisions()
                # Small delay to make the game smoother
                turtle.time.sleep(0.01)
            except turtle.Terminator:
                print("Turtle graphics window closed.")
                break

if __name__ == "__main__":
    try:
        game = PongGame()
        game.run()
    except turtle.Terminator:
        print("The game was terminated.")
