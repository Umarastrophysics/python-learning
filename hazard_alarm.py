"""
   emergency expiration custom alarm system
                                           """
def sound_alarm(chemical):    
    for i in range(10):
         print("dont use that chemical:" + chemical)                        
chemical = ["HCL","HF","Aqua_regia"]
expiration_timeline = (input("put how old is it:"))
if expiration_timeline == "1_month":
    print("use it soon it will expire")
elif expiration_timeline == "1_year":
    sound_alarm(chemical[1])

