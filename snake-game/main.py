import turtle
import time
import random


class SnakeGame:
    def __init__(self):
        self.setup_screen()
        self.snake = Snake()
        self.food = Food()
        self.score = ScoreBoard()
        self.bind_keys()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.snake.go_up, "Up")
        self.screen.onkey(self.snake.go_down, "Down")
        self.screen.onkey(self.snake.go_left, "Left")
        self.screen.onkey(self.snake.go_right, "Right")

    def run(self):
        while True:
            self.screen.update()
            self.snake.move()

            # Check for collision with food
            if self.snake.head.distance(self.food.food) < 20:
                self.food.refresh()
                self.snake.extend()
                self.score.increase_score()

            # Check for collision with wall
            if (self.snake.head.xcor() > 290 or self.snake.head.xcor() < -290 or
                    self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290):
                self.score.reset()
                self.snake.reset()

            # Check for collision with self
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 20:
                    self.score.reset()
                    self.snake.reset()

            time.sleep(0.1)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "stop"

    def create_snake(self):
        for i in range(3):
            self.add_segment((-20 * i, 0))

    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        if self.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        if self.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        if self.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        if self.direction == "right":
            self.head.setx(self.head.xcor() + 20)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "stop"


class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.food.goto(x, y)


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.display = turtle.Turtle()
        self.display.speed(0)
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.display.clear()
        self.display.write(f"Score: {self.score}  High Score: {self.high_score}", align="center",
                           font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 10
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    def reset(self):
        self.score = 0
        self.update_score()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
