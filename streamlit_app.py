import streamlit as st
#D:\OneDrive\Desktop\Projects>streamlit run login-app-files.py
def login():
    st.title("Login")
    enterusername=st.text_input("Please enter username to update system")
    enterpassword=st.text_input("Please enter password",type="password")
    if st.button("Check User"):
        file=open("userlist.csv","r")
        for line in file:
            lines = line.split(",")

            username = lines[0]
            password = lines[1]
            if enterusername == username:
                if enterpassword == password:
                    st.session_state.logged_in=True
                    st.success("Login Successful")              
            else:
                st.error("Invalid username or password")
        file.close()
def dashboard():      
    st.write("Welcome Admin")
    if st.button("Sign Out"):
        st.session_state.logged_in=False
    st.title("Dashboard")
    username=st.text_input("Please username to add ")
    password=st.text_input("Please enter password",type="password")
    if st.button("Add User"):
        file=open("userlist.csv","a")
        file.write("\n")
        file.write(username + "," + password)
        file.close()
        
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if st.session_state.logged_in:
    dashboard()
else:
    login()

#Before coding - pip install streamlit
#After coding - Run, cmd browse to file directory
#Then streamlit run nameoffile.py
