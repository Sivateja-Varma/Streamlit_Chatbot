import streamlit as st 

st.title('this is a test')

# dictStore={
#   'one':one,
#   'two':two,
#   'three',three
# }

if 'k' not in st.session_state:
  st.session_state['k']=10

with st.form(key='testForm'):
  st.header('test form')
  one=st.text_input('enter text: ')
  two=st.slider('this is just a test slider',min_value=200,max_value=1000)
  three=st.date_input(label='this is test date')

  submit=st.form_submit_button('submit')



if submit:
  st.session_state['k']+=1
  st.write(st.session_state['k'])
  st.write(submit,one,two,three)  

