votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

def add_vote():
    name = input("Enter candidate name: ")

    if name in votes:
        votes[name] += 1
        print("Vote added!\n")
    else:
        print("Candidate not found!\n")

def display_votes():
    print("\nCurrent Votes:")
    for candidate, count in votes.items():
        print(candidate, ":", count)
    print()

def find_winner():
    winner = max(votes, key=votes.get)
    print("Winner is:", winner, "with", votes[winner], "votes\n")

def menu():
    while True:
        print("Voting System")
        print("1. Add Vote")
        print("2. Show Votes")
        print("3. Show Winner")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_vote()
        elif choice == "2":
            display_votes()
        elif choice == "3":
            find_winner()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice")
menu()
