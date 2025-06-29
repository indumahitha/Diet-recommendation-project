import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data for nutritional information
nutrition_data = {
    'Nutrient': ['Protein', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals'],
    'Description': [
        'Essential for growth and repair of tissues. Good sources include meat, fish, dairy, beans, and nuts.',
        'Primary source of energy. Found in foods like bread, pasta, rice, fruits, and vegetables.',
        'Necessary for energy storage, hormone production, and cell function. Healthy sources include avocados, nuts, and olive oil.',
        'Vital for overall health and immune function. Found in a variety of fruits and vegetables.',
        'Important for bone health, muscle function, and overall wellness. Sources include dairy products, leafy greens, and nuts.'
    ]
}

# Sample data for macronutrient distribution in a balanced diet
diet_data = pd.DataFrame({
    'Nutrient': ['Protein', 'Carbohydrates', 'Fats'],
    'Percentage': [30, 50, 20]
})

# Sample data for vitamin and mineral intake
vitamins_minerals_data = pd.DataFrame({
    'Nutrient': ['Vitamin A', 'Vitamin C', 'Calcium', 'Iron'],
    'Recommended Daily Intake (mg)': [900, 90, 1000, 8]
})

def nutritional_info_page():
    st.title("Nutritional Information")

    st.header("General Nutrition Facts")
    st.markdown("""
    - **Protein**: Essential for growth and repair of tissues. Good sources include meat, fish, dairy, beans, and nuts.
    - **Carbohydrates**: Primary source of energy. Found in foods like bread, pasta, rice, fruits, and vegetables.
    - **Fats**: Necessary for energy storage, hormone production, and cell function. Healthy sources include avocados, nuts, and olive oil.
    - **Vitamins**: Vital for overall health and immune function. Found in a variety of fruits and vegetables.
    - **Minerals**: Important for bone health, muscle function, and overall wellness. Sources include dairy products, leafy greens, and nuts.
    """)

    st.header("Macronutrient Distribution in a Balanced Diet")
    st.dataframe(diet_data)

    fig, ax = plt.subplots()
    sns.barplot(x='Nutrient', y='Percentage', data=diet_data, palette='viridis', ax=ax)
    ax.set_title('Macronutrient Distribution')
    st.pyplot(fig)

    st.header("Recommended Daily Intake of Vitamins and Minerals")
    st.dataframe(vitamins_minerals_data)

    fig, ax = plt.subplots()
    sns.barplot(x='Nutrient', y='Recommended Daily Intake (mg)', data=vitamins_minerals_data, palette='plasma', ax=ax)
    ax.set_title('Recommended Daily Intake of Vitamins and Minerals')
    st.pyplot(fig)

    st.header("Interesting Nutrition Facts")
    st.markdown("""
    - **Water**: Essential for life. The human body is made up of approximately 60% water.
    - **Fiber**: Aids in digestion and helps prevent constipation. Good sources include fruits, vegetables, and whole grains.
    - **Antioxidants**: Help protect your cells from damage. Found in berries, nuts, and dark chocolate.
    - **Omega-3 Fatty Acids**: Important for brain health. Found in fatty fish like salmon and flaxseeds.
    """)

    st.header("Nutritional Value of Common Foods")
    common_foods_data = pd.DataFrame({
        'Food': ['Apple', 'Banana', 'Chicken Breast', 'Almonds', 'Broccoli'],
        'Calories': [95, 105, 165, 164, 55],
        'Protein (g)': [0.5, 1.3, 31, 6, 3.7],
        'Carbohydrates (g)': [25, 27, 0, 6, 11],
        'Fats (g)': [0.3, 0.3, 3.6, 14, 0.6]
    })

    st.dataframe(common_foods_data)

    fig, ax = plt.subplots()
    common_foods_data.plot(kind='bar', x='Food', ax=ax)
    ax.set_title('Nutritional Value of Common Foods')
    st.pyplot(fig)

    st.header("Healthy Eating Tips")
    st.markdown("""
    - **Eat a variety of foods**: Ensure you get all the necessary nutrients.
    - **Limit sugar and salt intake**: Excessive sugar and salt can lead to health issues.
    - **Stay hydrated**: Drink plenty of water throughout the day.
    - **Include plenty of fruits and vegetables**: Aim for at least 5 portions of fruits and vegetables a day.
    - **Choose whole grains over refined grains**: Whole grains are more nutritious and help maintain energy levels.
    - **Moderate portion sizes**: Be mindful of portion sizes to avoid overeating.
    - **Avoid processed foods**: Processed foods often contain unhealthy fats, sugars, and additives.
    """)

if __name__ == "__main__":
    nutritional_info_page()
