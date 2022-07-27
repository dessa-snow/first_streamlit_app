import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# st.text(fruityvice_response.json())

st.subheader("Fruityvice Fruit Advice!")
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)

# do not run anything past here
st.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# st.text("Hello from Snowflake:")
st.subheader("The fruit load list contains:")
st.dataframe(my_data_rows)

# Allow end user to add fruit to list
add_my_fruit = st.text_input('What fruit would you like to add?','Jackfruit')
st.write('Thanks for adding ', add_my_fruit)

# Add to Sf
my_cur.execute("insert into fruit_load_list values ('from streamlit')")


