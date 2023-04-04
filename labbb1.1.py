# Ask user for input
name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
cavity_filling = input("Was cavity-filling performed? (y/n): ")
xray = input("Was X-Ray performed? (y/n): ")

# Constants
CLEANING_RATE = 60
CAVITY_FILLING_RATE = 200
XRAY_RATE = 100
TAX_RATE = 0.15

# Function to calculate the total bill
def calculate_bill(name, cleaning, cavity_filling, xray):
    subtotal = 0
    if cleaning == 'y':
        subtotal += CLEANING_RATE
    if cavity_filling == 'y':
        subtotal += CAVITY_FILLING_RATE
    if xray == 'y':
        subtotal += XRAY_RATE

    tax = subtotal * TAX_RATE

    total_before_discount = subtotal + tax

    # Apply discount if total bill is more than $200 or $300
    if total_before_discount > 300:
        discount_rate = 0.1
    elif total_before_discount > 200:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = subtotal * discount_rate
    total = total_before_discount - discount

    # Print the receipt
    print("Melanie Dental Clinic")
    print("------------------------")
    print("Receipt for patient name:", name)
    print("----------------------------")
    print("Subtotal: $", subtotal)
    print("Tax: $", tax)
    print("----------------------------")
    print("Total: $", round(total, 2))



# Calculate and print the bill
calculate_bill(name, cleaning, cavity_filling, xray)
