import streamlit
streamlit.title('My parents new healthy diner')

streamlit.header('Menu')

streamlit.text('Crepes')
streamlit.text('Pancakes')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')




streamlit.dataframe(fruits_to_show)

streamlit.header("🍉Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")


# write your own comment -normalize json file data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - put it upfront
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

