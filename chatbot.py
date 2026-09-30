from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


def Inference(query:str,model:str,temp:float|int,api_key:str,max_tokens:int):
  template=ChatPromptTemplate.from_messages([
    ('system','you are a helpful chatbot'),
    ('user','{question}')
  ])
  llm=ChatOpenAI(model=model,temperature=temp,api_key=api_key,max_completion_tokens=max_tokens)
  output=StrOutputParser()
  chain=template|llm|output
  answer= chain.invoke({"question":query})
  return answer

# do not set the max_tokens too low will lead to empty outputs inference runs gets empty results with no error as technically it runs 
st.set_page_config(page_title='chatbot',layout='wide')
st.title("ChatBotV1")
st.sidebar.title('Tweak Menu')
api_key=st.sidebar.text_input('enter api key for inference',type='password')
temp=st.sidebar.slider('temp tweaker',min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider('max tokens',min_value=100,max_value=500,value=200)
model=st.sidebar.selectbox('select your model',options=['gpt-5.6-sol','gpt-5.6-terra','gpt-5.6-luna'])

with st.form(key='inference_form'):
  query=st.text_input('your query:')
  if query and api_key:
    with st.spinner('thinking...'):
      response=Inference(query,model,temp,api_key,max_tokens)
      st.write(response)
  elif query:
    st.warning('enter a valid api key')
  else:
    st.write("enter a input for inference")
  st.form_submit_button(label='Submit')  
