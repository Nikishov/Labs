from enum import Enum


class States(Enum):
    s0      = 's0'
    nxtlit  = 'nxtlit'
    stop    = 'stop'
    error   = 'error'

class Lexer():
    def __init__(self):
        self.current_state = States.s0
        self.s = []
        

    def check(self, char):
        match self.current_state:
            case States.s0:
                self.change_s0(char)
            case States.nxtlit:
                self.change_nxtlit(char)


    def change_s0(self, char):
        self.current_state = States.s0
        match char:
            case _ if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                self.change_nxtlit(char)
            case _ if char == ' ':
                self.s.append(char)
                self.current_state = States.s0
            case _ if char == '\n':
                self.change_nxtlit(char)
            case _ :  
                self.current_state = States.error


    def change_nxtlit(self, char):
        self.current_state = States.nxtlit
        match char:
            case _ if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                self.s.append(char)
            case _ if (char >= '0' and char <= '9'):
                self.s.append(char)
            case _ if char == ' ':
                self.change_s0(char)
            case _ if char == '\n':
                self.s.append(char)
            case _ :  
                self.current_state = States.error
                

def test():
    lex = Lexer()
    with open('test.txt') as f:
        for ch in f.read():
            if lex.current_state == States.error:
                print('Incorrect symbol in file!')
                break
            else:
                lex.check(ch)
    if lex.current_state != States.error:
        print(''.join(lex.s))

    lex.current_state = States.stop


test()
