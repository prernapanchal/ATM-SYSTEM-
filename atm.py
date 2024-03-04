Pin=7616
cb=10000
for i in range(3):
    p=int(input("Enter your pin"))
    if p==Pin:
          print("Welcome our bank")
          wb=int(input("Enter amount of withdraw"))
          if cb>wb:
             cb=cb-wb
          print("TRANSACTION SUCCESSFUL")
          print("Currrent balance is ",cb)
          print("EXIT YOUR CARD")
          break
    else:
          print("Incorrect pin")
else:
    print("You try more than so card is blocked")
