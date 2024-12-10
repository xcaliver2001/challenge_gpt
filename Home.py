import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime

#
today = datetime.today().strftime("%H:%M:%S")


st.title("Hello World!!")
st.subheader("Welcome to Streamlit!!")
st.markdown("""
            ### Let's dive into it.
#### I love it!!
            """)

a = [1,3,4,5]
d = {"x" : 1}

st.write("Hello")
st.write(a)
st.write(d)

st.write(PromptTemplate)

# magic
p = PromptTemplate.from_template("xxxx")

p
a
d

#2.Class - Dataflow

st.title(today)

model = st.selectbox("Choose your model", ("GPT-3", "GPT-4"),)
st.write(model)

if model == "GPT-3" : 
    st.write("cheap")

else : 
    st.write("not cheap")

name = st.text_input("What's your name?")
st.write(name)

value = st.slider(
    "temperature",
    min_value=0.1,
    max_value=1.0,
)

st.write(value)

#3.Multipage
with st.sidebar : 
    st.title("Menu")
    st.text("Me")
    st.text_input("Meme")


tab_one, tab_two, tab_three = st.tabs(["A", "B", "C"])

with tab_one : 
    st.write("A")

with tab_two : 
    st.write("B")

with tab_three : 
    st.write("C")
