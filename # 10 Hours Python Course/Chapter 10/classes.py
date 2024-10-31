
class Business:
    # This are the class attributes
    name = "MothaBusiness"
    profit = 1203456800000  
    loss = 500
    net_total = "profit"

manoj = Business()

print(Business.name, Business.profit, Business.net_total)
            #  OR
print(manoj.name, manoj.profit, manoj.net_total)

# This are the object attributes
manoj.future = "billion$"
Business.security = "100%"
print(manoj.security, manoj.future, manoj.name, manoj.profit, manoj.net_total)