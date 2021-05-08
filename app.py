# import streamlit as st
from model import modelHandler
from query_handler import Query

st.write("""
# Wisdom App. 
This app uses BERT base model to answer user input questions. It fetches the context for the question from internet. 
The answer is presented on streamlit UI. I am using Squad finetuned Bert large uncased model
Developed by : Shankar Kumar
Source code: https://github.com/kumarshankar/QnA_app
""")

st.subheader("Question")
question = st.text_input('Please enter your question here')
# question = "what is the color of the sky"

query = Query(question, 2)
context = query.get_context()
context = context[:1000] # for compute reasons select only top 1000 chars in context
print(context)

model = modelHandler("BERT")
st.subheader("Here's your answer")
answer = model.get_answer(question, context)
# print(answer)
st.write(answer)
