import random
import curses
import time
from art import *


class Snake:

    def __init__(self):
        snake_x = int(width / 4)
        snake_y = int(height / 2)
        self.snake = [
            [snake_y, snake_x],
            [snake_y, snake_x-1],
            [snake_y, snake_x-2]
        ]
        self.key = curses.KEY_RIGHT
        self.food = [int(height/2), int(width/2)]
        self.draw_food()
        self.move()

    def move(self):
        while True:
            self.press_key()

            if self.snake[0][0] in [-1, height] or self.snake[0][1] in [-1, width] or self.snake[0] in self.snake[1:]:
                self.finish_game()
            else:
                self.draw_snake()

    def press_key(self):
        next_key = window.getch()
        self.key = self.key if next_key == -1 else next_key

        new_head = [self.snake[0][0], self.snake[0][1]]
        if self.key == curses.KEY_DOWN:
            new_head[0] += 1
        if self.key == curses.KEY_UP:
            new_head[0] -= 1
        if self.key == curses.KEY_LEFT:
            new_head[1] -= 1
        if self.key == curses.KEY_RIGHT:
            new_head[1] += 1

        self.snake.insert(0, new_head)

    def draw_snake(self):
        if self.snake[0] == self.food:
            self.draw_food()
        else:
            tail = self.snake.pop()
            window.addch(int(tail[0]), int(tail[1]), ' ')

        window.addch(int(self.snake[0][0]), int(
            self.snake[0][1]), curses.ACS_CKBOARD)

    def draw_food(self):
        self.food = None
        while self.food is None:
            new_food = [
                random.randint(1, height - 1),
                random.randint(1, width - 1)
            ]
            self.food = new_food if new_food not in self.snake else None
        window.addch(self.food[0], self.food[1], curses.ACS_BLOCK)

    def finish_game(self):
        window.clear()
        window.refresh()
        Art = text2art("game over", "random")
        print(Art)
        time.sleep(5)
        curses.endwin()
        quit()


if __name__ == "__main__":
    s = curses.initscr()
    curses.curs_set(0)
    height, width = s.getmaxyx()
    window = curses.newwin(height, width, 0, 0)
    window.keypad(1)
    window.timeout(100)
    Snake = Snake()
