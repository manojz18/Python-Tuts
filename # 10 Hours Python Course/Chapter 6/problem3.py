p1 = "Make a lot of Money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter the message: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("SPAM, Call police")

else:
    print("Genuine Message")


