import streamlit as st
from multipage1 import MultiApp
from login1 import login_page
from weeklyplan1 import weekly_plan_page
from nutritionalinfo1 import nutritional_info_page
from progress1 import progress_page

# Initialize the MultiApp instance
app = MultiApp()

# Add all application pages here
app.add_app("Login", login_page)
app.add_app("Weekly Plan", weekly_plan_page)
app.add_app("Nutritional Information", nutritional_info_page)
app.add_app("Progress", progress_page)

# Define the sidebar navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Weekly Plan", "Nutritional Information", "Progress"])

    # Run the selected page
    if page == "Login":
        login_page()
    elif page == "Weekly Plan":
        if 'logged_in' in st.session_state and st.session_state['logged_in']:
            weekly_plan_page()
        else:
            st.warning("Please log in to access the Weekly Plan page.")
    elif page == "Nutritional Information":
        nutritional_info_page()
    elif page == "Progress":
        if 'logged_in' in st.session_state and st.session_state['logged_in']:
            progress_page()
        else:
            st.warning("Please log in to access the Progress page.")

# Run the sidebar navigation
sidebar_navigation()
