"""
   emergency expiration custom alarm system
                                            """
# Added the colon here!
def sound_alarm():    
    # Added the colon here!
    for i in range(10): 
         print("dont use that chemical")                        

chemicals = ["HCL","HF","Aqua_regia"]
expiration_timeline = input("put how old is it: ")

if expiration_timeline == "1_month":
    print("use it soon it will expire")
elif expiration_timeline == "1_year":
    sound_alarm()
