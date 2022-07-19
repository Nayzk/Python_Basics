from ast import While
from pickle import TRUE


class Game:
    def __init__(self):
        while TRUE:
            print('''
    Welcom to my game ..
    Choose the app you need..
        1 : Even & Odd of set of numbers
        2 : Number of words
        3 : Print specific numbers
        4 : Specific multiple number
        5 : Print all numbers accept multiple togather 
        6 : Press X to exit
    ''')

            user_choice = int(input('Enter your choice : '))
            if user_choice == 1:
                Enter = int(input('PLz enter your numbers : '))
                self.show_odd_even(Enter)
            elif user_choice == 2:
                sentence = input('Enter your words : ')
                self.count_words(sentence)
            elif user_choice == 3:
                x = int(input('Plz, enter your number : '))   
                self.count_numbers(x)
            elif user_choice == 4:
                st = int(input('Enter your first number : '))
                sc = int(input('Enter your second number : '))
                self.count_multiple(st,sc)
            elif user_choice == 5:
                st_no = int(input('Plz enter 1st number : '))
                sec_no = int(input('Plz enter 2nd number : '))
                self.residual_numbers(st_no,sec_no)

            play_again = input('Press any key to play again, N for Exit : ' )
            if play_again == 'N':
                break




    def show_odd_even(self,Enter):
        Even_l = [(x) for x in range(Enter+1) if x %2==0]
        print(Even_l)
        odd_l = [(x) for x in range(Enter+1) if x %2!=0]
        print(odd_l)

    def count_words(self,sentence):
        count_words = len(sentence.split())
        print(count_words)

    def count_numbers(self,x):
        [print (i) for i in range(0,x+1)]

    def count_multiple(self,st,sc):
        for x in range(0,st+1):
            if x %sc==0:
                print(x)

    def residual_numbers(self,st_no,sec_no):


        for x in range(0,101):
            if x % st_no ==0 and x % sec_no ==0:
                print(x)


g1 = Game()


