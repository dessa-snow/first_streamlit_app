import streamlit as st
import pandas as pd
import requests

st.title("My Parents New Healthy Diner")

st.subheader("Breakfast Favorites")
st.caption(":bowl_with_spoon: Omega 3 & Blueberry Oatmeal")
st.caption(":green_salad: Kale, Spinach & Rocket Smoothie")
st.caption(":egg: Hard-boiled Free-Range Egg")
st.caption(":avocado: Avocado Toast")

st.subheader(":banana: :grapes: Build Your Own Fruit Smoothie :watermelon: :strawberry:")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

# st.multiselect("Pick some fruits: ", list(my_fruit_list.index), ["Avocado", "Strawberries"])
# st.dataframe(my_fruit_list)

fruits_selected = st.multiselect("Pick some fruits: ", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# st.text(fruityvice_response.json())

st.subheader("Fruityvice Fruit Advice!")
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)

