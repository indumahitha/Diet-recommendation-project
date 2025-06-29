import streamlit as st
import pymongo
import bcrypt

# MongoDB connection using connection string from MongoDB Compass
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["diet_app"]
users_collection = db["users"]

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def login_page():
    st.title("Login/Signup")

    login_type = st.selectbox("Choose Login or Signup", ["Login", "Signup"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if login_type == "Signup":
        confirm_password = st.text_input("Confirm Password", type="password")
       
        if password != confirm_password:
            st.error("Passwords do not match")
            return

    if st.button("Submit"):
        if login_type == "Signup":
            if users_collection.find_one({"username": username}):
                st.error("Username already exists")
            else:
                hashed_password = hash_password(password)
                users_collection.insert_one({"username": username, "password": hashed_password})
                st.success("Signup successful!")
        else:
            user = users_collection.find_one({"username": username})
            if user and check_password(password, user['password']):
                st.success("Login successful!")
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                
            else:
                st.error("Invalid username or password")

if __name__ == "__main__":
    login_page()
