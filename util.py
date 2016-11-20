from user import *

userList = []

def parseTxt(name):
    f = open(name,"r")
    st = f.readline()
    
    result = []
    
    while st != "":
        if st[:st.find(",")] not in result:

            uName = st[:st.find(",")].strip()
            
            st = st[st.find(",") + 1:]
            password = st[:st.find(",")].strip()
            
            st = st[st.find(",") + 1:]
            accnt = st.strip()
            
            user = User(aType=accnt, pwd=password, name=uName)
            user.put()
            result.append(user)
            st = f.readline()
    
    return result

def getAccount(userName, uList):
    for i in range(len(uList)):
        if userName.strip() == uList[i].getName().strip():
            return uList[i]

def getInstrAccount(uList):
    for i in range(len(uList)):
        if uList[i].getaType() == "i":
            return uList[i]
    
    
    