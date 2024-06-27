import turtle
import random

# Player class
class Player:
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.color("green")
        self.player.penup()
        self.player.goto(0, -280)
        self.player.setheading(90)

    def move_up(self):
        self.player.forward(20)

    def move_down(self):
        if self.player.ycor() > -280:
            self.player.backward(20)

    def move_left(self):
        if self.player.xcor() > -380:
            self.player.setx(self.player.xcor() - 20)

    def move_right(self):
        if self.player.xcor() < 380:
            self.player.setx(self.player.xcor() + 20)

    def reset_position(self):
        self.player.goto(0, -280)

    def clear(self):
        self.player.clear()
        self.player.hideturtle()

# Car class
class Car:
    def __init__(self, speed_factor):
        self.car = turtle.Turtle()
        self.car.shape("square")
        self.car.color(random.choice(["red", "blue", "yellow", "purple", "orange"]))
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.penup()
        self.car.goto(400, random.randint(-250, 250))
        self.base_speed = random.randint(5, 15)
        self.speed_factor = speed_factor

    def move(self):
        self.car.backward(self.base_speed * self.speed_factor)

    def reset_position(self):
        if self.car.xcor() < -400:
            self.car.goto(400, random.randint(-250, 250))
            self.base_speed = random.randint(5, 15)

    def clear(self):
        self.car.clear()
        self.car.hideturtle()

    def update_speed_factor(self, speed_factor):
        self.speed_factor = speed_factor

# ScoreBoard class
class ScoreBoard:
    def __init__(self):
        self.current_score = 0
        self.highest_score = 0
        self.difficulty_level = 1
        self.display = turtle.Turtle()
        self.display.speed(0)
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.display.clear()
        self.display.write(f"Score: {self.current_score}  High Score: {self.highest_score}  Level: {self.difficulty_level}",
                           align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.current_score += 1
        self.difficulty_level = self.current_score + 1
        self.update_score()

    def reset_score(self):
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score
        self.current_score = 0
        self.difficulty_level = 1
        self.update_score()

    def clear(self):
        self.display.clear()

# TurtleCrossingGame class
class TurtleCrossingGame:
    def __init__(self):
        self.setup_screen()
        self.player = Player()
        self.speed_factor = 1
        self.cars = [Car(self.speed_factor) for _ in range(10)]
        self.scoreboard = ScoreBoard()
        self.bind_keys()
        self.game_over_display = turtle.Turtle()
        self.game_over_display.speed(0)
        self.game_over_display.color("red")
        self.game_over_display.penup()
        self.game_over_display.hideturtle()
        self.game_over = False
        self.run()

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("Turtle Crossing Road")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkeypress(self.player.move_up, "Up")
        self.screen.onkeypress(self.player.move_down, "Down")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")

    def check_collisions(self):
        for car in self.cars:
            if self.player.player.distance(car.car) < 20:
                self.game_over = True
                return True
        return False

    def check_win(self):
        if self.player.player.ycor() > 280:
            self.player.reset_position()
            self.scoreboard.increase_score()
            self.speed_factor += 1  # Increase the speed factor more noticeably
            self.update_car_speeds()
            return True
        return False

    def update_car_speeds(self):
        for car in self.cars:
            car.update_speed_factor(self.speed_factor)

    def show_game_over(self):
        self.game_over_display.goto(0, 0)
        self.game_over_display.write("Game Over", align="center", font=("Courier", 36, "normal"))

    def clear_screen(self):
        self.player.clear()
        for car in self.cars:
            car.clear()
        self.scoreboard.clear()
        self.game_over_display.clear()

    def reset_game(self):
        self.clear_screen()
        self.game_over = False
        self.player = Player()
        self.speed_factor = 1  # Reset the speed factor
        self.cars = [Car(self.speed_factor) for _ in range(10)]
        self.scoreboard.reset_score()
        self.bind_keys()

    def run(self):
        while True:
            self.screen.update()
            for car in self.cars:
                car.move()
                car.reset_position()
            if self.check_collisions():
                self.show_game_over()
                self.screen.update()
                turtle.time.sleep(2)
                self.reset_game()
            if self.check_win():
                print("You Win!")
            turtle.time.sleep(0.1)

if __name__ == "__main__":
    game = TurtleCrossingGame()
    turtle.done()
