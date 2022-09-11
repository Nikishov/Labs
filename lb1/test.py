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
        self.s = []

    def send(self, char):
        if self.current_state == States.s0:
            if self.first_try:
                if (char >= '0' and char <= '9'):
                    self.current_state = States.nxtlit
                elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                    self.current_state = States.nxtlit
                elif char == ' ':
                    self.s.append(char)
                    self.current_state = States.s0
                elif char == '\n':
                    self.current_state = States.nxtlit
                else:
                    self.current_state = States.error

            else:
                if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                    self.current_state = States.nxtlit
                elif char == ' ':
                    self.s.append(char)
                    self.current_state = States.s0
                elif char == '\n':
                    self.current_state = States.nxtlit
                else:
                    self.current_state = States.error

        if self.current_state == States.nxtlit:
            if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                self.s.append(char)
                self.current_state = States.nxtlit
            elif (char >= '0' and char <= '9'):
                self.s.append(char)
                self.current_state = States.nxtlit
            elif char == ' ':
                self.s.append(char)
                self.first_try = True
                self.current_state = States.s0
            elif char == '\n':
                self.s.append(char)
                self.current_state = States.nxtlit
            else:
                self.current_state = States.error


        self.current_state = States.stop
                

def grep_regex():
    lex = Lexer()
    with open('test.txt') as f:
        for ch in f.read():
            if lex.current_state == States.error:
                print('Некоректный символ в файле')
                break
            else:
                lex.send(ch)
    if lex.current_state != States.error:
        print(''.join(lex.s))

grep_regex()

