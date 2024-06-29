day = "wednesday"
age = 12
ticket_price = 12 if age >= 13 else 8

if day == "wednesday":
    ticket_price -= 2

print("Your ticket price $", ticket_price)

# ticket_price = 0
# if age <= 0:
#     print("Enter your correct age")
# else:
#     if age < 13:
#         ticket_price = 8
#     else:
#         ticket_price = 12

#     if day == "wednesday":
#         ticket_price -= 2

#     print("Your ticket price: ", ticket_price)
