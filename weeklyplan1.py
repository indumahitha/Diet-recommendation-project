
import streamlit as st
import random
import pandas as pd
from pymongo import MongoClient

# Define diet and exercise plans
lose_weight_plans = [
    {
        "goal": "Lose weight",
        "day": "Monday",
        "breakfast": "Oats upma with vegetables",
        "lunch": "Grilled chicken salad with cucumber and tomato",
        "dinner": "Stir-fried vegetables with paneer and brown rice",
        "water_intake": "Drink at least 8 glasses of water per day",
        "exercise": "40 minutes of brisk walking and 20 minutes of yoga",
        "type": "non-veg"
    },
    {
        "goal": "Lose weight",
        "day": "Monday",
        "breakfast": "Oats upma with vegetables",
        "lunch": "Grilled vegetable salad with cucumber and tomato",
        "dinner": "Stir-fried vegetables with paneer and brown rice",
        "water_intake": "Drink at least 8 glasses of water per day",
        "exercise": "40 minutes of brisk walking and 20 minutes of yoga",
        "type": "veg"
    },
    {
        "goal": "Lose weight",
        "day": "Tuesday",
        "breakfast": "Whole grain toast with avocado and poached eggs",
        "lunch": "Quinoa with roasted vegetables and tofu",
        "dinner": "Baked fish with quinoa and steamed spinach",
        "water_intake": "Drink at least 8 glasses of water per day",
        "exercise": "45 minutes of cycling and 15 minutes of stretching",
        "type": "non-veg"
    },
    {
        "goal": "Lose weight",
        "day": "Tuesday",
        "breakfast": "Whole grain toast with avocado and poached eggs",
        "lunch": "Quinoa with roasted vegetables and tofu",
        "dinner": "Baked tofu with quinoa and steamed spinach",
        "water_intake": "Drink at least 8 glasses of water per day",
        "exercise": "45 minutes of cycling and 15 minutes of stretching",
        "type": "veg"
    },
    {
    "goal": "Lose weight",
    "day": "Wednesday",
    "breakfast": "Smoothie with spinach, banana, and protein powder",
    "lunch": "Turkey and avocado wrap with a side salad",
    "dinner": "Grilled shrimp with couscous and sautéed zucchini",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "30 minutes of running and 30 minutes of strength training",
    "type": "non-veg"
},
{
    "goal": "Lose weight",
    "day": "Wednesday",
    "breakfast": "Smoothie with spinach, banana, and protein powder",
    "lunch": "Avocado wrap with a side salad",
    "dinner": "Grilled tofu with couscous and sautéed zucchini",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "30 minutes of running and 30 minutes of strength training",
    "type": "veg"
},
{
    "goal": "Lose weight",
    "day": "Thursday",
    "breakfast": "Greek yogurt with honey and walnuts",
    "lunch": "Chicken and vegetable stir-fry",
    "dinner": "Grilled tilapia with quinoa and steamed broccoli",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "40 minutes of swimming and 20 minutes of yoga",
    "type": "non-veg"
},
{
    "goal": "Lose weight",
    "day": "Thursday",
    "breakfast": "Greek yogurt with honey and walnuts",
    "lunch": "Vegetable stir-fry with tofu",
    "dinner": "Grilled tofu with quinoa and steamed broccoli",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "40 minutes of swimming and 20 minutes of yoga",
    "type": "veg"
},
{
    "goal": "Lose weight",
    "day": "Friday",
    "breakfast": "Whole wheat pancakes with fresh fruits",
    "lunch": "Grilled tofu with brown rice and stir-fried vegetables",
    "dinner": "Salmon with sweet potato and steamed asparagus",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "45 minutes of cycling and 15 minutes of core exercises",
    "type": "non-veg"
},
{
    "goal": "Lose weight",
    "day": "Friday",
    "breakfast": "Whole wheat pancakes with fresh fruits",
    "lunch": "Grilled tofu with brown rice and stir-fried vegetables",
    "dinner": "Grilled tofu with sweet potato and steamed asparagus",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "45 minutes of cycling and 15 minutes of core exercises",
    "type": "veg"
},
{
    "goal": "Lose weight",
    "day": "Saturday",
    "breakfast": "Egg white omelette with spinach and whole wheat toast",
    "lunch": "Cauliflower rice stir-fry with tofu and vegetables",
    "dinner": "Grilled turkey burger with quinoa salad",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "60 minutes of hiking or outdoor activities",
    "type": "non-veg"
},
{
    "goal": "Lose weight",
    "day": "Saturday",
    "breakfast": "Egg white omelette with spinach and whole wheat toast",
    "lunch": "Cauliflower rice stir-fry with tofu and vegetables",
    "dinner": "Grilled veggie burger with quinoa salad",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "60 minutes of hiking or outdoor activities",
    "type": "veg"
},
{
    "goal": "Lose weight",
    "day": "Sunday",
    "breakfast": "Chia seed pudding with almond milk and berries",
    "lunch": "Chickpea and vegetable curry with brown rice",
    "dinner": "Baked cod with roasted potatoes and green beans",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "Rest day or light stretching and meditation",
    "type": "non-veg"
},
{
    "goal": "Lose weight",
    "day": "Sunday",
    "breakfast": "Chia seed pudding with almond milk and berries",
    "lunch": "Chickpea and vegetable curry with brown rice",
    "dinner": "Baked tofu with roasted potatoes and green beans",
    "water_intake": "Drink at least 8 glasses of water per day",
    "exercise": "Rest day or light stretching and meditation",
    "type": "veg"
}

]

build_muscle_plans =  [
    {
        "goal": "Build muscle",
        "day": "Monday",
        "breakfast": "Greek yogurt with granola and fruits",
        "lunch": "Lean beef steak with sweet potato and steamed broccoli",
        "dinner": "Salmon fillet with quinoa and roasted asparagus",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "45 minutes of weight training (focus on major muscle groups) and 15 minutes of HIIT",
        "type": "non-veg"
    },
    {
        "goal": "Build muscle",
        "day": "Monday",
        "breakfast": "Greek yogurt with granola and fruits",
        "lunch": "Grilled paneer steak with sweet potato and steamed broccoli",
        "dinner": "Grilled tofu fillet with quinoa and roasted asparagus",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "45 minutes of weight training (focus on major muscle groups) and 15 minutes of HIIT",
        "type": "veg"
    },
    {
        "goal": "Build muscle",
        "day": "Tuesday",
        "breakfast": "Smoothie with protein powder, spinach, and berries",
        "lunch": "Grilled chicken with brown rice and steamed vegetables",
        "dinner": "Turkey meatballs with whole wheat pasta and salad",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "60 minutes of weightlifting and bodyweight exercises",
        "type": "non-veg"
    },
    {
        "goal": "Build muscle",
        "day": "Tuesday",
        "breakfast": "Smoothie with protein powder, spinach, and berries",
        "lunch": "Grilled tofu with brown rice and steamed vegetables",
        "dinner": "Veggie meatballs with whole wheat pasta and salad",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "60 minutes of weightlifting and bodyweight exercises",
        "type": "veg"
    },
   
    {
        "goal": "Build muscle",
        "day": "Wednesday",
        "breakfast": "Protein pancakes with Greek yogurt and berries",
        "lunch": "Chicken breast with quinoa and roasted vegetables",
        "dinner": "Beef stir-fry with brown rice",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "60 minutes of weightlifting and bodyweight exercises",
        "type": "non-veg"
    },
    {
        "goal": "Build muscle",
        "day": "Wednesday",
        "breakfast": "Smoothie with protein powder, spinach, and almond milk",
        "lunch": "Grilled tofu with quinoa and mixed vegetables",
        "dinner": "Vegetable stir-fry with tofu and brown rice",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "60 minutes of weightlifting and bodyweight exercises",
        "type": "veg"
    },
    {
        "goal": "Build muscle",
        "day": "Thursday",
        "breakfast": "Scrambled eggs with whole grain toast and avocado",
        "lunch": "Grilled chicken with sweet potato and steamed broccoli",
        "dinner": "Salmon fillet with quinoa and roasted asparagus",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "45 minutes of weight training and 15 minutes of HIIT",
        "type": "non-veg"
    },
    {
        "goal": "Build muscle",
        "day": "Thursday",
        "breakfast": "Greek yogurt with granola and fruits",
        "lunch": "Grilled paneer steak with sweet potato and steamed broccoli",
        "dinner": "Grilled tofu fillet with quinoa and roasted asparagus",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "45 minutes of weight training and 15 minutes of HIIT",
        "type": "veg"
    },
    {
        "goal": "Build muscle",
        "day": "Friday",
        "breakfast": "Smoothie with protein powder, spinach, and berries",
        "lunch": "Grilled chicken with brown rice and steamed vegetables",
        "dinner": "Turkey meatballs with whole wheat pasta and salad",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "60 minutes of weightlifting and bodyweight exercises",
        "type": "non-veg"
    },
    {
        "goal": "Build muscle",
        "day": "Friday",
        "breakfast": "Chia seed pudding with almond milk and berries",
        "lunch": "Quinoa with roasted vegetables and tofu",
        "dinner": "Baked tofu with quinoa and steamed spinach",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "60 minutes of weightlifting and bodyweight exercises",
        "type": "veg"
    },
    {
        "goal": "Build muscle",
        "day": "Saturday",
        "breakfast": "Greek yogurt with granola and fruits",
        "lunch": "Lean beef steak with sweet potato and steamed broccoli",
        "dinner": "Salmon fillet with quinoa and roasted asparagus",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "45 minutes of weight training and 15 minutes of HIIT",
        "type": "non-veg"
    },
    {
        "goal": "Build muscle",
        "day": "Saturday",
        "breakfast": "Smoothie with protein powder, spinach, and berries",
        "lunch": "Grilled tofu with brown rice and steamed vegetables",
        "dinner": "Veggie meatballs with whole wheat pasta and salad",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "45 minutes of weight training and 15 minutes of HIIT",
        "type": "veg"
    },
    {
        "goal": "Build muscle",
        "day": "Sunday",
        "breakfast": "Greek yogurt with granola and fruits",
        "lunch": "Lean beef steak with sweet potato and steamed broccoli",
        "dinner": "Salmon fillet with quinoa and roasted asparagus",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "Rest day or light stretching and meditation",
        "type": "non-veg"
    },
    {
        "goal": "Build muscle",
        "day": "Sunday",
        "breakfast": "Chia seed pudding with almond milk and berries",
        "lunch": "Chickpea and vegetable curry with brown rice",
        "dinner": "Baked tofu with roasted potatoes and green beans",
        "water_intake": "Drink at least 10 glasses of water per day",
        "exercise": "Rest day or light stretching and meditation",
        "type": "veg"
    }
]


def suggest_weekly_plan(goal, diet_type, gender):
    if goal == "Lose Weight":
        selected_plans = [plan for plan in lose_weight_plans if plan["type"] == diet_type]
    elif goal == "Build Muscle":
        selected_plans = [plan for plan in build_muscle_plans if plan["type"] == diet_type]
    else:
        selected_plans = []

    # Filter by gender if specified
    if gender == "male":
        selected_plans = [plan for plan in selected_plans if "female" not in plan.get("exclude_gender", [])]
    elif gender == "female":
        selected_plans = [plan for plan in selected_plans if "male" not in plan.get("exclude_gender", [])]

    random.shuffle(selected_plans)
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    weekly_plan = []
    for day in days_of_week:
        day_plan = next((plan for plan in selected_plans if plan["day"] == day), None)
        if day_plan:
            weekly_plan.append(day_plan)
    
    return weekly_plan

def weekly_plan_page():
    st.title("Weekly Diet and Exercise Planner")

    # Initialize session state
    if 'username' not in st.session_state:
        st.session_state.username = None

    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['diet_app']
    users_collection = db['users']  # Collection for user details

    height = st.number_input('Height (cm)', min_value=0.0)
    weight = st.number_input('Weight (kg)', min_value=0.0)
    age = st.number_input('Age', min_value=0)
    goals = st.selectbox('Health Goals', ['Lose Weight', 'Build Muscle'])
    diet_type = st.radio("Diet Type", ('veg', 'non-veg'))
    gender = st.radio("Gender", ('male', 'female'))

    save_button = st.button('Save Details')

    if save_button:
        # Save user details to MongoDB
        user_details = {
            'username': st.session_state.username,
            'height': height,
            'weight': weight,
            'age': age,
            'goals': goals,
            'diet_type': diet_type,
            'gender': gender
        }
        users_collection.insert_one(user_details)
        st.success('Details saved successfully!')

    if st.button("Generate Weekly Plan"):
        if not (goals and height and weight and diet_type and gender):
            st.error("Please fill in all required fields (Goal, Height, Weight, Diet Type, Gender) to generate the weekly plan.")
        else:
            weekly_plan = suggest_weekly_plan(goals, diet_type, gender)
            
            if weekly_plan:
                st.subheader("Weekly Plan:")
                df = pd.DataFrame(weekly_plan)
                st.table(df.set_index('day').drop(columns=['goal', 'type']))
            else:
                st.error("No plans available for this goal or input combination.")

if __name__ == '__main__':
    weekly_plan_page()

