def get_valid_score(prompt):
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

scores = []
print("=== Enter 5 Initial Scores (0 - 100) ===")
for i in range(1, 6):
    valid_score = get_valid_score(f"Enter score #{i}: ")
    scores.append(valid_score)

original_scores = scores.copy()
while True:
    print("\n" + "=" * 35)
    print("         SCORE MANAGER MENU")
    print("=" * 35)
    print("1.  Display Scores")
    print("2.  Add Score")
    print("3.  Insert Score")
    print("4.  Remove Score")
    print("5.  Remove Last Score")
    print("6.  Search Score")
    print("7.  Generate Statistics")
    print("8.  Sort Scores")
    print("9.  Reverse Scores")
    print("10. Clear Scores")
    print("11. Restore Original Scores")
    print("12. Exit")
    print("=" * 35)

    choice = input("Enter your choice (1-12): ").strip()

    if choice == "1":
        if scores:
            print("Current Scores:", scores)
        else:
            print("The score list is currently empty.")

    elif choice == "2":
        new_score = get_valid_score("Enter score to add (0-100): ")
        scores.append(new_score)
        print(f"Added {new_score}. Updated list: {scores}")

    elif choice == "3":
        new_score = get_valid_score("Enter score to insert (0-100): ")
        while True:
            try:
                idx = int(input(f"Enter index (0 to {len(scores)}): "))
                if 0 <= idx <= len(scores):
                    scores.insert(idx, new_score)
                    print(f"Inserted {new_score} at index {idx}. Updated list: {scores}")
                    break
                else:
                    print(f"Invalid index! Must be between 0 and {len(scores)}.")
            except ValueError:
                print("Invalid input! Please enter an integer index.")

    elif choice == "4":
        if not scores:
            print("Cannot remove: The score list is empty.")
        else:
            target = get_valid_score("Enter score to remove: ")
            if target in scores:
                scores.remove(target)
                print(f"Removed first occurrence of {target}. Updated list: {scores}")
            else:
                print(f"Score {target} not found in the list.")

    elif choice == "5":
        if not scores:
            print("Cannot remove: The score list is empty.")
        else:
            removed = scores.pop()
            print(f"Removed last score: {removed}. Updated list: {scores}")

    elif choice == "6":
        if not scores:
            print("The score list is empty.")
        else:
            target = get_valid_score("Enter score to search: ")
            if target in scores:
                count = scores.count(target)
                first_idx = scores.index(target)
                print(f"Score {target} found! Count: {count}, First Index: {first_idx}")
            else:
                print(f"Score {target} not found.")

    elif choice == "7":
        if not scores:
            print("Cannot generate statistics: The score list is empty.")
        else:
            count = len(scores)
            total = sum(scores)
            average = total / count
            highest = max(scores)
            lowest = min(scores)
            print("\n--- Score Statistics ---")
            print(f"Count:   {count}")
            print(f"Total:   {total}")
            print(f"Average: {average:.2f}")
            print(f"Highest: {highest}")
            print(f"Lowest:  {lowest}")

    elif choice == "8":
        if not scores:
            print("The score list is empty; nothing to sort.")
        else:
            order = input("Sort order - (A)scending or (D)escending? ").strip().lower()
            if order in ("a", "ascending"):
                scores.sort()
                print("Scores sorted in ascending order:", scores)
            elif order in ("d", "descending"):
                scores.sort(reverse=True)
                print("Scores sorted in descending order:", scores)
            else:
                print("Invalid sort order! Please enter 'A' or 'D'.")

    elif choice == "9":
        if not scores:
            print("The score list is empty; nothing to reverse.")
        else:
            scores.reverse()
            print("Scores reversed:", scores)

    elif choice == "10":
        scores.clear()
        print("All scores have been cleared.")

    elif choice == "11":
        scores = original_scores.copy()
        print("Original scores restored:", scores)

    elif choice == "12":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid menu choice! Please select a number from 1 to 12.")
