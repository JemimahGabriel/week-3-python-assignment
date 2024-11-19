def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount_percentage)

    if final_price == original_price:
        print(f"No discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"After applying the discount, the final price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")