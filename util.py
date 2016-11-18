from user import User

userList = []

def parseTxt(name):
    f = open(name,"r")
    st = f.readline()
    
    result = []
    
    while st != "":
        if st[:st.find(",")] not in result:

            uName = st[:st.find(",")]
            
            st = st[st.find(",") + 1:]
            password = st[:st.find(",")]
            
            st = st[st.find(",") + 1:]
            accnt = st
            
            user = User(aType=accnt, pwd=password, name=uName)
            result.append(user)
            st = f.readline()
    
    return result

def getAccount(userName):
    for i in range(len(userList)):
        if i.getName() == userName:
            return i
            
    return None
