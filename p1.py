import streamlit as st
st.title('Title -> Geeks for Geeks')
st.header('header -> Geeks for Geeks')
st.subheader('subheader -> Geeks for Geeks')
st.text('text -> Geeks for Geeks')
st.markdown('Geeks')
st.markdown('# Geeks')
st.markdown('## Geeks')
st.markdown('### Geeks')
st.markdown('#### Geeks')
st.markdown('##### Geeks')
st.success('data submitted successfully')
st.info('information')
st.warning('warning')
st.error('error')

exp=ZeroDivisionError('division not possible by 0')
st.exception(exp)
st.help(Exception)
st.write("1+2+3")
st.write(1+2+3)
st.code('x=10\n'
        'for i in range(x):\n'
         '\t print(i)\n')
if st.checkbox('male'):
    st.write('you are male')
st.checkbox('female')
radiobutton=st.radio('select : ',('male','female','others'))
if radiobutton=='male':
    st.write('you are male')
elif radiobutton=='female':
    st.write('you are female')
else:
    st.write('you are neither male nor female')
    
multiselectbox=st.multiselect("data science : ", ['data analysis','web scraping','ML','deep learning','NPL','computer vision','image processing'])
st.write('you have choosen : ',multiselectbox,len(multiselectbox))
if st.button('click me'):
    st.write('you clicked me')
level=st.slider('select the level',1,10,step=1)
st.write('level is : ',level)
username=st.text_input('enter your username : ')
password=st.text_input('enter your password : ',type='password')
st.write('hi',username)
textarea=st.text_area('write something about yourself in 500 words')
st.write(textarea)
st.number_input('select your age',18,110)
st.date_input('date')
st.time_input('Time')
