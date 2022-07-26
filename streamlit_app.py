import streamlit as st
import pandas as pd

st.title("My Parents New Healthy Diner")

st.subheader("Breakfast Favorites")
st.caption(":bowl_with_spoon: Omega 3 & Blueberry Oatmeal")
st.caption(":green_salad: Kale, Spinach & Rocket Smoothie")
st.caption(":egg: Hard-boiled Free-Range Egg")
st.caption(":avocado: Avocado Toast")

st.subheader(":banana: :grapes: Build Your Own Fruit Smoothie :watermelon: :strawberry:")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
