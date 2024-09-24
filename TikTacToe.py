# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 01:13:48 2023

@author: Aadil
"""
import sys
import random

class menu:
    def __init__(self):
       self.menuChoice = self.checkGameMode()
    

    def getUserInput(self):
        try: 
            self.menuChoice = int(input('Enter one of the choices 1, 2, 3:  '))
            if self.menuChoice > 0 and self.menuChoice <= 3:
                return self.menuChoice
            else:
                print('Invalid Input, Please Enter 1, 2 or 3')
                self.getUserInput()
        except ValueError:
            print('Wrong input please enter a number between 1 and 3')
            self.getUserInput()
    def checkGameMode(self):
        self.getUserInput()
        if self.menuChoice == 1:
            mode = SinglePlayerMode()
            return mode
        elif self.menuChoice == 2:
            mode = TwoPlayerMode()
            return mode
        else:
            sys.exit("The game has been terminated")

class SinglePlayerMode:
    def __init__(self):
        print("Single Player Mode")
        self.outputBoxHelp()
        self.inputs = []
        self.userinp = []
        self.cpuinp = []
        self.placeToken()
        
    def getUserTokenInput(self):
        while True:
            try:
                user = int(input('Player X which box you would like to place ur token into: '))
            
                if user > 0 and user <=9:
                    if user in self.inputs:
                        print('Choice is already taken')
                        user = int(input('Player X which box you would like to place ur token into: '))
                    else:
                        self.inputs.append(user)
                        self.userinp.append(user)
                        return user
                else:
                        print('Incorrect Choice, enter a number between 1 and 9')
                        user = int(input('Player X which box you would like to place ur token into: '))
            except ValueError:
                print('Wrong input please enter a number between 1 and 9')
                continue
               
    def getCPUchoice(self):
        
        x = random.randrange(1,10)
        while True:
            
            if x in self.inputs:
                x = random.randrange(1,10)
            
            elif x not in self.inputs:
                self.inputs.append(x)
                self.cpuinp.append(x)
                return x
        
        
    def checkWin(self,player):

        winCom = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in winCom:
            if all(y in player for y in x):
                return True
       
        return False
    
   
    
    def placeToken(self):
        values = [' ' for x in range(9)]
        while True:
           
            self.outputBox(values)
            
            if self.checkWin(self.cpuinp):
                print('CPU has won the game')
                break
            elif self.checkWin(self.userinp):
                print('You have won the game')
                break
            
            if len(self.inputs) == 9:
                if self.checkWin(self.userinp):
                    self.outputBox(values)
                    print('You has won the game')
                    break
                else:
                    print('You have Drawn')
                    break
            else:
                values[self.getUserTokenInput()-1] = 'X'
            
            if len(self.inputs) == 9:
                if self.checkWin(self.cpuinp):
                    self.outputBox(values)
                    print('CPU has won the game')
                    self.outputBox(values)
                    break
                else:
                    print('You have Drawn')
                    self.outputBox(values)
                    break
            else:
                values[self.getCPUchoice()-1] = 'O'
    
    def outputBoxHelp(self):
        print("The boxes are numbered as shown below ")
        
        print("\n")
        print("\t     |     |")
        print("\t  1  |  2  |  3")
        print('\t_____|_____|_____')
 
        print("\t     |     |")
        print("\t  4  |  5  |  6")
        print('\t_____|_____|_____')
 
        print("\t     |     |")
 
        print("\t  7  |  8  |  9")
        print("\t     |     |")
        print("\n")
    
        print('You are token X')
    
        
        
    def outputBox(self,values):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
        print('\t_____|_____|_____')
 
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
        print('\t_____|_____|_____')
 
        print("\t     |     |")
 
        print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
        print("\t     |     |")
        print("\n")
        
        
        
        
        
        
        
        
class TwoPlayerMode(SinglePlayerMode):
     def __init__(self):
        print("Two Player Mode")
        self.outputBoxHelp()
        self.inputs = []
        self.userinp = []
        self.user2inp = []
        self.placeToken()
        
        
     def getOtherUserchoice(self):
        while True:
            try:
                    user = int(input('Player O which box you would like to place ur token into: '))
            
                    if user > 0 and user <=9:
                        if user in self.inputs:
                            print('Choice is already taken')
                            user = int(input('Player O which box you would like to place ur token into: '))
                        else:
                            self.inputs.append(user)
                            self.user2inp.append(user)
                            return user
                    else:
                        print('Incorrect Choice, Enter a number between 1 and 9')
                        user = int(input('Player O which box you would like to place ur token into: '))
            except ValueError:
                print('Wrong input please enter a number between 1 and 9')
                continue
    
     def placeToken(self):
        values = [' ' for x in range(9)]
        while True:
           
            self.outputBox(values)
            
            if self.checkWin(self.userinp):
                print('Player X has won the game')
                break
            elif self.checkWin(self.user2inp):
                print('Player O has won the game')
                break
            
            if len(self.inputs) == 9:
                if self.checkWin(self.userinp):
                    self.outputBox(values)
                    print('Player X has won the game')
                    break
                else:
                    print('You have Drawn')
                    break
            else:
                values[self.getUserTokenInput()-1] = 'X'
                self.outputBox(values)
            if len(self.inputs) == 9:
                if self.checkWin(self.user2inp):
                    self.outputBox(values)
                    print('Player O has won the game')
                    self.outputBox(values)
                    break
                else:
                    print('You have Drawn')
                    self.outputBox(values)
                    break
            else:
                values[self.getOtherUserchoice()-1] = 'O'

def outputMenu():
    print('Welcome To Tik Tack Toe, Select one of the options below')
    print('\n    1: Single Player Mode')
    print('    2: Two Player Mode')
    print('    3: Exit Game')

if __name__ == "__main__":
    outputMenu()
    tictactoe = menu()
