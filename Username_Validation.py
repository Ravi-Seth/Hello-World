class User_validation:
    print ("------User name should be at least 6 digits----")
    def __init__(self,uname):
        self.uname=uname
        upper=0
        lower=0
        digit=0
        length=(len(self.uname))
        if (length >=6):
            for element in self.uname:
                if (element.isupper()):
                    upper=upper+1
                    
                if (element.islower()):
                    lower=lower+1
                    
                if (element.isdigit()):
                    digit=digit+1
            if (upper > 0 and lower > 0 and digit > 0):
                print (f"{self.uname} is a valid Username")
            else:
                print (f"{self.uname} is an invalid Username")
        else:
            print (f"{self.uname} uname length can't be less than 6")

User_validation("Dino9")
User_validation("Dino9a9")
User_validation("Ajaxcloud3")

            
