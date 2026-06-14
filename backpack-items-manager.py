""" inventry system 
                 """
inventry = ["candy","choclate","rocket toy","protien bars","chicken","electric stove","20kg bag of flour","1kg salt"]
inventry.extend (["phone","charger"])
inventry.append ("power bank")
print("inventry has: ", inventry )
item_to_be_used = input("what item you want to utalize: ")
if item_to_be_used in inventry:
  inventry.remove(item_to_be_used)
  print(f"you used this item: {item_to_be_used}")
else: 
  print(f"you dont have: {item_to_be_used}")
print(inventry)
