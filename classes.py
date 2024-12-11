
price = int(input("Enter item's price: "))
discount_percent = int(input("Enter the discount: "))

def  calculate_discount(price, discount_percent):
  if discount_percent >=20:
    return price - (price * discount_percent/100)
  else: 
    return price

final_price = calculate_discount(price, discount_percent)
print(f"the final price is {final_price}")