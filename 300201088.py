# Functions
def prepareInfo(filename):
    # Open the file and read its contents
    with open(filename, 'r') as file:
        # Split each line by ';' and strip whitespace, then store in a list
        items = [line.strip().split(';') for line in file.readlines()]
    return items
def printMenu(items):
    # Print each item in the list with its corresponding number
    i = 1
    for item in items:
        print(f"{i}. {item[1]}")
        i += 1
def getUserInput(prompt, max_value):
    # Keep asking for input until a valid number within the range is given
    while True:
        value = int(input(prompt))
        if 1 <= value <= max_value:
            return value
        else:
            print("Invalid input. Please try again.")
# Main program
order = []
total_cost = 0.0
while True:
    print("--------------------------------------------------")
    print("Welcome to the Store")
    print("--------------------------------------------------")
    # Prepare the categories from the categories.txt file
    categories = prepareInfo('categories.txt')
    # Print the menu of categories
    printMenu(categories)
    # Ask the user to select a category
    category = getUserInput("Please select the category: ", len(categories))
    # Prepare the products from the products.txt file
    products = prepareInfo('products.txt')
    # Filter the products based on the selected category
    products_filtered = [product for product in products if product[0] == f"#{category}"]
    # Print the menu of filtered products
    printMenu(products_filtered)
    # Ask the user to select a product
    product = getUserInput("Please select the product: ", len(products_filtered))
    # Prepare the portions from the portions.txt file
    portions = prepareInfo('portions.txt')
    # Filter the portions based on the selected product
    portions_filtered = [portion for portion in portions if portion[0] == "#" + products_filtered[product-1][2]]
    # Print the menu of filtered portions
    printMenu(portions_filtered)
    # Ask the user to select a portion
    portion = getUserInput("Please select the portion: ", len(portions_filtered))
    # Assume the cost is the last item in the portion string
    # Add the cost to the total cost
    cost = float(portions_filtered[portion-1][-1])
    total_cost += cost
    # Add the order to the list of orders
    order.append(f"{categories[category-1][1]} {products_filtered[product-1][1]} {portions_filtered[portion-1][1]} {cost}$")
    # Ask the user if they want to complete the order
    complete = input("Would you like to complete the order (y, n)? ")
    if complete.lower() == 'y':
        break
# Print the order recipe
print("--------------------------------------------------")
print("Order Recipe")
print("==============================================================")
for item in order:
    print(item)
print("==============================================================")
# Print the total cost
print(f"Total: {total_cost}$")