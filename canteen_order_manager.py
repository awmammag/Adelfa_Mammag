menu = []

for i in range(5):
    menu.append(input(f"Enter order {i+1}:"))

print("Original orders", menu)

menu.append(input(f"Enter additional order: "))
print("Updated orders", menu)

prioritize = input(f"Enter prioritized order: ")

menu.insert(0, menu.pop(menu.index(prioritize)))
print("Updated list:", menu)

search_item = input("Search for a food item: ")
if search_item in menu:
    count = menu.count(search_item)
    first_idx = menu.index(search_item)
    print(f"Found '{search_item}'! Count: {count}, First index: {first_idx}")
else:
    print("Order not found.")

cancel_item = input("Enter an order to cancel: ")
menu.remove(cancel_item)
print(f"Canceled '{cancel_item}'. Updated orders: {menu}")

removed_order = menu.pop()
print(f"Removed last order: {removed_order}")

menu.sort()
print(f"Final orders: {menu}")
print(f"Total remaining orders: {len(menu)}")