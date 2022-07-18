from getpass import getpass # for taking password as input
import sys
import platform # to check the OS
import os # for running commands in the terminal

# importing modules
from config.connection import connect
from login import login
from create_account import create_account
from deposit import deposit
from withdraw import withdraw
from update_info import update_info
from delete_account import delete_account
from show_stats import show_stats

if platform.system()=="Windows":
    os.system("cls")
elif platform.system()=="Linux" or platform.system()=="Darwin":
    os.system("clear")


print("Welcome to Py Bank.\n")

print("Connecting to db...")
collection=connect() # returns the collection in db
print("Connected.")

print("\nPress\n1. Create Account.\n2. Update Information.\n3. Deposit\n4. Withdraw\n5. Show Current Balance.\n6. Delete Account.\n7. Show Stats.\n8. Exit\n")

choice=int(input())

matched_account=None

def check_balance(matched_account):
    print("\nCurrent Balance: %.2f\n" %matched_account["balance"])

# --- Creating Account ---
if choice==1:
    create_account(collection)

# --- Update Info ---
if choice==2:
    matched_account=login(collection)
    if matched_account is not None:
        update_info(collection, matched_account)

# --- Deposit ---
if choice==3:
    matched_account=login(collection)
    if matched_account is not None:
        amount=float(input("Enter amount to deposit: "))
        deposit(collection, matched_account, amount)

# --- Withdraw ---
if choice==4:
    matched_account=login(collection)
    if matched_account is not None:
        amount=float(input("Enter amount to withdraw: "))
        withdraw(collection, matched_account, amount)

# show current balance
if choice==5:
    matched_account=login(collection)
    check_balance(matched_account)

# delete account
if choice==6:
    matched_account=login(collection)
    if matched_account is not None:
        delete_account(collection, matched_account)

# show stats
if choice==7:
    matched_account=login(collection)
    if matched_account is not None:
        show_stats(collection, matched_account)
        

# --- Exit ---
if choice==8:
    print("\nExiting App...\n")
    sys.exit(0)