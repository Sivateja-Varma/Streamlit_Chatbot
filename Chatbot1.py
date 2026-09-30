from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

def Inference(query:str,model:str,temp:float|int,max_tokens:int):
  template=ChatPromptTemplate.from_messages([
    ('system','you are a helpful chatbot'),
    ('user','{question}')
  ])
  llm=ChatOllama(model=model,temperature=temp,num_predict=max_tokens)
  output=StrOutputParser()
  chain=template|llm|output
  answer= chain.invoke({"question":query})
  return answer

# do not set the max_tokens too low will lead to empty outputs inference runs gets empty results with no error as technically it runs 
st.set_page_config(page_title="ChatBotV1", layout="wide")
st.title("ChatBotV1")
st.sidebar.title('Tweak Menu')
temp=st.sidebar.slider('temp tweaker',min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider('max tokens',min_value=100,max_value=500,value=200)
model=st.sidebar.selectbox('select your model',options=['gemma2:2b','qwen3:1.7b','deepseek-r1:1.5b'])


with st.form('modelRun'):
  query=st.text_input('your query:')
  if query:
    with st.spinner('thinking...'):
      response=Inference(query,model,temp,max_tokens)
      st.write(response)
  else:
    st.write("enter a input for inference")
  st.form_submit_button('submit')  
