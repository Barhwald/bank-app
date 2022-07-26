import time
import sys
import random

class banking_app:
    def __init__(self, initial_ammount=0.00):
        self.balance = initial_ammount

    def transactionLog(self, log):
        with open('log.txt', 'a') as file:
            file.write(f"{log}\n")

    def delay_print(self, s):
        for letter in s:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)

    def askUser(self):
        option = input('\n\t\t\t\t\tWhat would you like to do?\nType:\n"1" for deposit\n"2" for withdrawal\n"3" for checking balance\n"4" for quitting\n"5" for a random dad joke\n')
        return option

    def deposit(self):
        income = input('How much would you like to deposit? ')

        try:
            income = float(income)
        except ValueError:
            income = 0
        if income:
            if income > 0:
                self.balance = self.balance + income
                self.transactionLog(f"You deposited {income}. \tBalance: {self.balance}")
            else:
                self.delay_print("You cannot deposit a negative ammount.")

    def withdraw(self):
        outcome = input('How much would you like to withdraw? ')
        try:
            outcome = float(outcome)
        except ValueError:
            outcome = 0
        if outcome:
            if outcome > 0:
                if outcome > self.balance:
                    self.delay_print(f"Not enough funds.\nThe maximum you can withdraw is {self.balance} USD")
                else:
                    self.balance = self.balance - outcome
                    self.transactionLog(f"You withdrew {outcome}. \tBalance: {self.balance}")
            else: self.delay_print("You cannot withdraw a negative ammount.")

    def delay_print_balance(self, s="Your current balance is: "):
        txt = s + str(self.balance) + " USD"
        for letter in txt:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)

    def dad_joke(self):
        jokes_list = ["Yesterday I tried to catch fog. Mist..\n", "I'm afraid for the calendar. Its days are numbered.\n", "What did the ocean say to the beach?\nNothing, it just waved.\n", "I only know 25 letters of the alphabet. I don't know y.\n", "Why couldn't the bicycle stand up by itself?\nIt was two tired.\n", "Did you hear the rumor about butter?\nWell, I'm not going to spread it!\n", "Why didn't the skeleton climb the mountain?\nIt didn't have the guts.\n", "Together we will rice. Lettuce pray. Ramen.\n", "I used to be addicted to soap, but I'm clean now.\n", "What country's capital is growing the fastest?\nIreland. Every day it's Dublin.\n", "I once had a dream I was floating in an ocean of orange soda. It was more of a fanta sea.\n", "Mountains aren't just funny. They're hill areas.\n"]
        a = random.choice(jokes_list)
        self.delay_print(a)

account = banking_app()

print("\n\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\t\t\t\t$                                     $\n\t\t\t\t$         Welcome to our bank!        $\n\t\t\t\t$                                     $\n\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

while True:
    account_action = account.askUser()
    if account_action == '1':
        account.deposit()

    if account_action == '2':
        account.withdraw()

    if account_action == '3':
        account.delay_print_balance()

    if account_action == '4':
        print("\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\t\t\t\t$                                     $\n\t\t\t\t$  Thank you for using our services!  $\n\t\t\t\t$                                     $\n\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        break

    if account_action == '5':
        account.dad_joke()
