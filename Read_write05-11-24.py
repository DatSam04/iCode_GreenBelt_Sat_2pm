import os
from datetime import datetime

DIARY_FILE = "diary.txt"

def write_entry():
    entry = input("Write your diary entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = open(DIARY_FILE, "a")
    file.write(f"\n\n{timestamp}\n{entry}")

def read_entries():
    if not os.path.exists(DIARY_FILE) or os.path.getsize(DIARY_FILE) == 0:
        print("No entries found.")
    else:
        file = open(DIARY_FILE, "r")
        entries = file.read().strip().split("\n\n")
        print(entries)

        print("Past Diary Entries:\n")
        for i in range(len(entries)):
            entry = entries[i].split("\n")
            timeEntry = entry[0]
            noteEntry = entry[1]
            print("{}. \n Date: {} \n Note: {} \n".format(i+1, timeEntry, noteEntry))


print("Welcome to My Secret Diary!\n")
while True:
    print("Main Menu:")
    print("1. Write a new diary entry")
    print("2. Read past diary entries")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")