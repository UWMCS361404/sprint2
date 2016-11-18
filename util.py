from user import User

userList = []

def parseTxt(name):
    f = open(name,"r")
    st = f.readline()
    
    result = []
    
    while st != "":
        if st[:st.find(",")] not in result:
            user = User()
            user.setName(st[:st.find(",")])
            
            st = st[st.find(",") + 1:]
            user.setPwd(st[:st.find(",")])
            
            st = st[st.find(",") + 1:]
            user.setaType(st)
            
            result.append(user)
            st = f.readline()
        
    return result

def getAccount(userName):
    
    for i in range(len(userList)):
        if i.getName() == userName:
            return i
            
    return None