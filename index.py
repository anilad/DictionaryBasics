dict = {}
dict["name"] = "Dalina Dao"
dict["age"] = 25
dict["country of birth"] = "The United States"
dict["favorite language"] = "Python"

def aboutMe(dict):
    for key,value in dict.iteritems():
        print "My {} is {}".format(key, value)

aboutMe(dict)