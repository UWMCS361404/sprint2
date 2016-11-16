from user import User

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
    