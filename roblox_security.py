"""
    basic
           roblox secourity system
                                   login system
                                                 via pasword
                                                             and
                                                                 f-strings as well"""
players = ["jimmy","timmy","mummy","bummy","billy","silly"]
players.extend (["karl","nolan"])
def secourity_alarm():
    for i in range(12):
        print("secourity compromised")
id = input("what is your roblox id: ")
password = (input("what is your password"))
if id == "roblox" and password == "gemini":
    print(f"you have owner panel and ability to ban players id: {id}")
elif id == "admin1234" and password == "gpt":
    print (f"you are an admin have abilty to ban players admin panel id: {id}")
elif id in players and password == "1234":
    print(f"welcome id: {id}")
else:
    secourity_alarm()
