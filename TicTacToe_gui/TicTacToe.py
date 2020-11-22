import turtle


class TicTacToe():
    def __init__(self):
        self.win = turtle.Screen()
        self.win.setup(700, 700)
        self.win.title('TicTacToe')

        self.create_game()

        while True:
            try:
                self.game()
            except:
                break

    def create_game(self):
        self.win.tracer(0)
        self.win.bgcolor('black')

        self.board = turtle.Turtle()
        self.board.color('red')
        self.board.pensize(10)
        self.board.penup()
        self.board.goto(100, 300)
        self.board.right(90)
        self.board.pendown()
        self.board.forward(600)
        self.board.penup()
        self.board.goto(-100, 300)
        self.board.pendown()
        self.board.forward(600)
        self.board.penup()
        self.board.goto(-300, 100)
        self.board.left(90)
        self.board.pendown()
        self.board.forward(600)
        self.board.penup()
        self.board.goto(-300, -100)
        self.board.pendown()
        self.board.forward(600)

        self.turn = 'x'
        self.winner = None
        self.is_game_over = False
        self.pieces_board = [None, None, None,
                             None, None, None, None, None, None]

    def set_move(self, x, y):
        if -100 < x < 100 and -100 < y < 100 and self.pieces_board[4] == None:
            self.draw_shape(4, 0, 0)

        elif -100 < x < 100 and 100 < y < 300 and self.pieces_board[1] == None:
            self.draw_shape(1, 0, 200)
        elif 100 < x < 300 and -100 < y < 100 and self.pieces_board[5] == None:
            self.draw_shape(5, 200, 0)
        elif -100 < x < 100 and -300 < y < -100 and self.pieces_board[7] == None:
            self.draw_shape(7, 0, -200)
        elif -300 < x < -100 and -100 < y < 100 and self.pieces_board[3] == None:
            self.draw_shape(3, -200, 0)

        elif -300 < x < -100 and 100 < y < 300 and self.pieces_board[0] == None:
            self.draw_shape(0, -200, 200)
        elif 100 < x < 300 and 100 < y < 300 and self.pieces_board[2] == None:
            self.draw_shape(2, 200, 200)
        elif -300 < x < -100 and -300 < y < -100 and self.pieces_board[6] == None:
            self.draw_shape(6, -200, -200)
        elif 100 < x < 300 and -300 < y < -100 and self.pieces_board[8] == None:
            self.draw_shape(8, 200, -200)

    def draw_shape(self, box, x, y):
        shape = turtle.Turtle()
        shape.speed(None)
        shape.color('green')
        shape.ht()
        shape.pensize(10)
        shape.penup()
        self.pieces_board[box] = self.turn
        if self.turn == 'x':
            shape.goto(x-75, y+75)
            shape.pendown()
            shape.right(45)
            shape.forward(212)
            shape.penup()
            shape.goto(x+75, y+75)
            shape.pendown()
            shape.right(90)
            shape.forward(212)
            shape.penup()
            self.turn = 'o'
        else:
            shape.goto(x, y-75)
            shape.pendown()
            shape.circle(75)
            shape.penup()
            self.turn = 'x'
        self.game_over()

    def game_over(self):
        # diagonals
        if self.pieces_board[0] == self.pieces_board[4] == self.pieces_board[8] and self.pieces_board[0] != None and self.pieces_board[4] != None and self.pieces_board[8] != None:
            self.is_game_over = True
        elif self.pieces_board[2] == self.pieces_board[4] == self.pieces_board[6] and self.pieces_board[2] != None and self.pieces_board[4] != None and self.pieces_board[6] != None:
            self.is_game_over = True
        # cols
        elif self.pieces_board[0] == self.pieces_board[3] == self.pieces_board[6] and self.pieces_board[0] != None and self.pieces_board[3] != None and self.pieces_board[6] != None:
            self.is_game_over = True
        elif self.pieces_board[1] == self.pieces_board[4] == self.pieces_board[7] and self.pieces_board[1] != None and self.pieces_board[4] != None and self.pieces_board[7] != None:
            self.is_game_over = True
        elif self.pieces_board[2] == self.pieces_board[5] == self.pieces_board[8] and self.pieces_board[2] != None and self.pieces_board[5] != None and self.pieces_board[8] != None:
            self.is_game_over = True
        # rows
        elif self.pieces_board[0] == self.pieces_board[1] == self.pieces_board[2] and self.pieces_board[0] != None and self.pieces_board[1] != None and self.pieces_board[2] != None:
            self.is_game_over = True
        elif self.pieces_board[3] == self.pieces_board[4] == self.pieces_board[5] and self.pieces_board[3] != None and self.pieces_board[4] != None and self.pieces_board[5] != None:
            self.is_game_over = True
        elif self.pieces_board[6] == self.pieces_board[7] == self.pieces_board[8] and self.pieces_board[6] != None and self.pieces_board[7] != None and self.pieces_board[8] != None:
            self.is_game_over = True

    def reset_game(self, x, y):
        self.win.clear()
        self.create_game()

    def game(self):
        if not self.is_game_over:
            self.win.update()
            self.win.onscreenclick(None, 3)
            self.win.onscreenclick(self.set_move, 1)
        else:
            self.winner = 'x' if self.turn == 'o' else 'o'
            show_winner = turtle.Turtle()
            show_winner.ht()
            show_winner.pencolor('white')
            show_winner.write(f'{self.winner} wins!'.upper(),
                              font=('verdana', 100), align='center')
            show_winner_aux = turtle.Turtle()
            show_winner_aux.ht()
            show_winner_aux.goto(0, -50)
            show_winner_aux.pencolor('cyan')
            show_winner_aux.write('right click to play again'.upper(),
                                  font=('verdana', 30), align='center')
            self.win.onscreenclick(None, 1)
            self.win.onscreenclick(self.reset_game, 3)


if __name__ == '__main__':
    ttc = TicTacToe()
