import streamlit as st

#st.write('Hola Ale. Está funcionado ya parece!')
with st.form("my_form"):
   st.write("pregunta")
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("pregunta recibida")

st.write("afuera")
