import turtle

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
        self.ball.speed(40)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.15  # Ball's speed in x direction
        self.ball.dy = 0.15  # Ball's speed in y direction

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def bounce_y(self):
        self.ball.dy *= -1

    def bounce_x(self):
        self.ball.dx *= -1

    def reset_position(self):
        self.ball.goto(0, 0)
        self.bounce_x()

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
        self.bind_keys()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

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
            self.screen.update()
            self.ball.move()
            self.check_collisions()

if __name__ == "__main__":
    game = PongGame()
    game.run()
