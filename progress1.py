import streamlit as st
from pymongo import MongoClient

def progress_page():
    st.title('Progress Page')

    # Initialize session state
    if 'username' not in st.session_state:
        st.session_state.username = None

    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['diet_app']  # Replace with your database name
    users_collection = db['users']  # Collection for user details
    progress_collection = db['progress']  # Collection for progress tracking

    # Progress logic
    initial_weight = st.number_input('Initial Weight (kg)', min_value=0.0)
    current_weight = st.number_input('Current Weight (kg)', min_value=0.0)

    calculate_button = st.button('Calculate Progress')

    if calculate_button:
        if initial_weight <= current_weight:
            st.error('Seems like you have gained weight if that is not your required goal Stick to your diet to see better progress!')
        else:
            # Calculate progress
            weight_change = initial_weight - current_weight
            if weight_change > 0:
                progress_percent = (weight_change / initial_weight) * 100
                progress_type = 'Weight Loss'
            else:
                progress_percent = abs(weight_change) / initial_weight * 100
                progress_type = 'Muscle Gain'

            # Save progress to MongoDB
            user_query = {'username': st.session_state.username}
            user_record = users_collection.find_one(user_query)

            if user_record:
                progress_data = {
                    'user_id': user_record['_id'],
                    'initial_weight': initial_weight,
                    'current_weight': current_weight,
                    'progress_percent': progress_percent,
                    'progress_type': progress_type
                }
                progress_collection.insert_one(progress_data)

                # Display progress message
                st.success(f'You have achieved {progress_percent:.2f}% {progress_type}! Keep it up!')

if __name__ == '__main__':
    progress_page()
