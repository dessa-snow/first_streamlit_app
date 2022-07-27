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
# st.write('The user entered ', fruit_choice)
# st.text(fruityvice_response.json())

# create function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

st.subheader("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)

except URLError as e:
  st.error()

# do not run anything past here
st.stop()

# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# st.text("Hello from Snowflake:")

st.subheader("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()
    
# Add button
if st.button("Get Fruit Load List"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.dataframe(my_data_rows)

# Allow end user to add fruit to list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values ('from streamlit')")
       return 'Thanks for adding ' + new_fruit
    
add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button("Add a fruit to list"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  st.text(back_from_function



