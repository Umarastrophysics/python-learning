"""
    basic
         roblox secourity system
                                login system
                                            via pasword
                                                 """
players = ["jimmy","timmy","mummy","bummy","billy","silly"]
players.extend (["karl","nolan"])
def secourity_alarm():
    for i in range(12):
        print("secourity compromised")
id = input("what is your roblox id: ")
password = (input("what is your password"))
if id == "roblox" and password == "gemini":
    print("you have owner panel and ability to ban players")
elif id == "admin1234" and password == "gpt":
    print ("you are an admin have abilty to ban players admin panel")
elif id == "players" and password == "1234":
    print("welcome players")
else:
    secourity_alarm()
