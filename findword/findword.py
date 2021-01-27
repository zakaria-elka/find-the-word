#-*-coding:Latin-1 -*
import os
import random
from random_word import RandomWords


class pendu:

    def __init__(self):
        self.choice =random.choice(open("word.txt", "r").readline().split())
        ii = 1
        for self.lx in self.choice:
                                   self.lx = ii * "*"
                                   ii += 1
        self.copylx =list(self.lx)

    def wordfind(self):
        i=1
        while i<=(len(self.choice)+2):
                   x=input("insert 1 letter: ").lower()
                   j=0
                   for l in self.choice :
                                          if l==x:
                                                     self.copylx[j]=x
                                                     print("great:  ",''.join(self.copylx))
                                                     break
                                          j=j+1

                   else:
                        print("slowly yu will get it")

                   if ''.join(self.copylx)==self.choice:
                                                         score =5+(len(''.join(self.copylx))-i)
                                                         print("Your score: ", score, "/5")
                                                         break

                   i=i+1

        else:
             print("game over")


print ("let's go")

while True:

            while True:
                       try:
                           name = input("put your name: ")
                           if type(name) != str:
                                                 raise ValueError

                           break
                       except ValueError:
                                         print("incorrect name")


            p=pendu()
            p.wordfind()
            newg = input('Replay put r // Exit put q : ')

            if newg.lower() != 'r':
                                     print("End game")
                                     break







os.system("pause")