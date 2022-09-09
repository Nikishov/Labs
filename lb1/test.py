from enum import Enum


class States(Enum):
    s0      = 's0'
    nxtlit  = 'nxtlit'
    stop    = 'stop'
    error   = 'error'

class Lexer():
    def __init__(self):
        self.current_state = States.s0
        self.first_try = False

    def send(self, char):

        if self.current_state == States.s0:
            if self.first_try:
                if (char >= '0' and char <= '9'):
                    self.current_state = States.nxtlit

            else:
                if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                    self.current_state = States.nxtlit
                elif char == ' ':
                    print(f'{char} - пробел')
                    self.current_state = States.s0
                elif char == '\n':
                    print('Перенос строки')
                    self.current_state = States.nxtlit
                else:
                    self.current_state = States.error

        if self.current_state == States.nxtlit:
            if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                print(f'{char} - буква')
                self.current_state = States.nxtlit
            elif (char >= '0' and char <= '9'):
                print(f'{char} - цифра')
                self.current_state = States.nxtlit
            elif char == ' ':
                print(f'{char} - пробел')
                self.first_try = True
                self.current_state = States.s0
            elif char == '\n':
                print('Перенос строки')
                self.current_state = States.nxtlit
            else:
                self.current_state = States.error
                print('Некорректный символ')

        if self.current_state == States.stop:
            print('Завершение')
            return

        if self.current_state == States.error:
            print('Ошибка')
            return

def grep_regex():
    lex = Lexer()
    with open('test.txt') as f:
        for ch in f.read():
            lex.send(ch)

grep_regex()

