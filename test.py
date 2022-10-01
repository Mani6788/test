import streamlit
streamlit.title("My parents new healthy diner")
streamlit.header( "Breakfast menu ")
streamlit.text("omega 3  and black berry oatmeal")
streamlit.text('kale ,spinach & rocket smoothie')
streamlit.text('hard boiled freerange egg') 

streamlit.header("Build you own fruit smoothie")
import pandas
my_fruits_list =pandas.read_csv( "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect ("pick some fruits", list(my_fruits_list.index))
streamlit.dataframe(my_fruits_list)
