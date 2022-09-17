# import module
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio



# Title
st.title("Triangle Plot Tool")

st.header('Upload csv with data')

data_file = st.file_uploader("Upload CSV with Mineral % values",type=["csv"])
		
if data_file is not None:

    file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
			
    st.write(file_details)
    df1 = pd.read_csv(data_file)
    st.dataframe(df1)

st.header('Plot Triangle Diagram')

q = st.selectbox(
'Pick your qtz column',
(df1.columns))

k = st.selectbox(
'Pick your k-feldspar column',
(df1.columns))

p = st.selectbox(
'Pick your Plagioclase column',
(df1.columns))

tcolor = st.selectbox(
'Pick your color column',
(df1.columns))

pio.templates.default = "presentation"
fig24 = px.scatter_ternary(df1, a=q, b=k, c=p, color=tcolor)


 
col1, col2 = st.columns(2)
col1.plotly_chart(fig24)



image = Image.open("qap_triangle.jpg")

col2.image(image, caption='Plutonic Rock Triangle source: https://i.pinimg.com/736x/4f/91/9c/4f919ccb976cd8edcd643da3cfbf76b3--igneous-rock-geology.jpg')

#col2.plotly_chart(fig25)

#-----------------------------------------------------
st.header("What type of rock is it classified as? (in progress)")
st.markdown("Enter values from left to right below")

col1, col2, col3 = st.columns(3)
#Temnp
#kspar = 1

qtz = col1.number_input('Enter Qtz %', 0, 100)
kspar = col2.number_input('Enter K-Feldspar %', 0, 100 - qtz, 1)
plag = col3.number_input('Enter Plagioclase %', 100 - (qtz + kspar), 100 - (qtz + kspar))





if qtz + kspar + plag > 100:
    st.error('you inputted values that add up to more than 100%')

data = {'Qtz':  [qtz],
        'K-spar': [kspar],
        'Plag':[plag]
        }

df = pd.DataFrame(data)

st.dataframe(df)
spar = 100 - qtz
st.success("Feldspar % is :"+ str(spar))



  
fig = px.scatter_ternary(df, a='Qtz', b='K-spar', c='Plag')


col1, col2 = st.columns(2)

col1.plotly_chart(fig)


image = Image.open("qap_triangle.jpg")

col2.image(image, caption='Plutonic Rock Triangle')

#------------------------------------------------------------------------
#Classify what type of rock it is
result = ' '

if qtz > 90:
    result = 'Quartzolite'
    
if qtz == 90:
    result = 'Quartzolite or Quartz-rich Granitoid'
    
if qtz <= 90 and qtz >= 60:
    result = 'Quartz-rich Granitoid'

# Tonalite
if qtz >= 20 and qtz <= 60:
    if (plag / spar) >= 0.9 :
        if qtz == 20:
            result = 'Quartz Diorite/Quartz Gabbro or '
        #result = result + 'Tonalite'
        
        if qtz == 60:
            result = 'Quartz-rich Granitoid or '
            
        if (plag / spar) == 0.9:
            result = 'Granodiorite or '
            
        result = result + 'Tonalite'
     
#Granodiorite     
if qtz >= 20 and qtz <= 60:
    if (plag / spar) >= 0.65 and (plag / spar) <= 0.9 :
        if qtz == 20:
            result = 'Quartz monzodiorite/monzoGabbro or '
        #result = result + 'Tonalite'
        
        if qtz == 60:
            result = 'Quartz-rich Granitoid or '
            
        if (plag / spar) == 0.65:
            result = 'Granite or '
            
        result = result + 'Granodiorite'
        
#Granite        
if qtz >= 20 and qtz <= 60:
    if (plag / spar) <= 0.65 and (plag / spar) >= 0.1 :
        if qtz == 20:
            result = 'Quartz monzonite or '
        #result = result + 'Tonalite'
        
        if qtz == 60:
            result = 'Quartz-rich Granitoid or '
            
        if (plag / spar) == 0.1:
            result = 'Alkali feldspar Granite or'
            
        result = result + 'Granite'
        
#Alkali feldspar Granite        
if qtz >= 20 and qtz <= 60:
    if (plag / spar) <= 0.1:
        if qtz == 20:
            result = 'Alkali Feldspar Quartz syenite or '
        #result = result + 'Tonalite'
        
        if qtz == 60:
            result = 'Quartz-rich Granitoid or '
            
        #if (plag / spar) == 0.1:
            #result = 'Alkali feldspar Granite or'
            
        result = result + 'Alkali feldspar Granite'
        
        
        
#Quartz Diorite       
if qtz <= 20 and qtz >= 5:
    if (plag / spar) >= 0.9:
        if qtz == 20:
            result = 'Tonalite or '
        #result = result + 'Tonalite'
        
        if qtz == 5:
            result = 'Diorite/Gabbro or '
            
        if (plag / spar) == 0.9:
            result = 'Quartz monzodiorite/monzoGabbro or '
            
        result = result + 'Quartz Diorite/ Quartz Gabbro'
     
     
#Quartz MonzoDiorite or Monzogabbro      
if qtz <= 20 and qtz >= 5:
    if (plag / spar) >= 0.65 and (plag / spar) <= 0.9:
        if qtz == 20:
            result = 'Granodiorite or '
        
        if qtz == 5:
            result = 'monzodiorite/monzoGabbro or '
            
        if (plag / spar) == 0.65:
            result = 'Quartz monzonite or '
            
        result = result + 'Quartz MonzoDiorite/MonzoGabbro '
        
        
#Quartz Monzonite     
if qtz <= 20 and qtz >= 5:
    if (plag / spar) <= 0.65 and (plag / spar) >= 0.35:
        if qtz == 20:
            result = 'Granite or '
        
        if qtz == 5:
            result = 'Monzonite or '
            
        if (plag / spar) == 0.35:
            result = 'Quartz Syenite or '
            
        result = result + 'Quartz Monzonite  '
        
        
#Quartz Syenite    
if qtz <= 20 and qtz >= 5:
    if (plag / spar) >= 0.1 and (plag / spar) <= 0.35:
        if qtz == 20:
            result = 'Granite or '
        
        if qtz == 5:
            result = 'Syenite or '
            
        if (plag / spar) == 0.1:
            result = 'Alkali Feldspar Quartz syenite or '
            
        result = result + 'Quartz Syenite  '
        
        
#AF Quartz Syenite    
if qtz <= 20 and qtz >= 5:
    if (plag / spar) <= 0.1 :
        if qtz == 20:
            result = 'Alkali Feldspar Granite or '
        
        if qtz == 5:
            result = 'Alkali Feldspar Syenite or '
            
        #if (plag / spar) == 0.1:
            #result = 'Quartz syenite or '
            
        result = result + 'Alkali Feldspar Quartz Syenite  '
        
        
#Diorite/Gabbro  
if qtz <= 5:
    if (plag / spar) >= 0.9:
        if qtz == 5:
            result = 'Quartz Diorite/ Quartz Gabbro or '
        
            
        if (plag / spar) == 0.9:
            result = 'monzodiorite/monzoGabbro or '
            
        result = result + 'Diorite/Gabbro  '



#monzodiorite/monzoGabbro    
if qtz <= 5:
    if (plag / spar) >= 0.65 and (plag / spar) <= 0.9:
        if qtz == 5:
            result = 'Quartz monzodiorite/monzoGabbro or '
        
            
        if (plag / spar) == 0.65:
            result = 'Monzonite or '
            
        result = result + 'Quartz monzodiorite/monzoGabbro '

#monzonite    
if qtz <= 5:
    if (plag / spar) <= 0.65 and (plag / spar) >= 0.35:
        if qtz == 5:
            result = 'Quartz monzonite or '
        
            
        if (plag / spar) == 0.35:
            result = 'Syenite or '
            
        result = result + 'Monzonite '
        
        
#Syenite    
if qtz <= 5:
    if (plag / spar) <= 0.35 and (plag / spar) >= 0.1:
        if qtz == 5:
            result = 'Quartz syenite or '
        
            
        if (plag / spar) == 0.1:
            result = 'Alkali Feldspar Syenite or '
            
        result = result + 'Syenite '


#AF Syenite    
if qtz <= 5:
    if (plag / spar) <= 0.1:
        if qtz == 5:
            result = 'Alkali Feldspar Quartz syenite or '
        
            
        #if (plag / spar) == 0.1:
            #result = 'Syenite or '
            
        result = result + 'Alkali Feldspar Syenite '







     
# if qtz >= 20 and qtz <= 60:

    # if kspar != 1:
        # if (kspar/ plag) > 0.9 :
            # if qtz == 20:
                # result = 'Quartz Diorite/Quartz Gabbro or '
            # #result = result + 'Tonalite'
            
            # if qtz == 60:
                # result = 'Quartz-rich Granitoid or '
            # result = result + 'Tonalite'
            
        # if (kspar / plag) > 0.65 and (kspar / plag) < 0.9 :
            # if qtz == 20:
                # result = 'Quartz Diorite/Quartz Gabbro or '
            # #result = result + 'Tonalite'
            
            # if qtz == 60:
                # result = 'Quartz-rich Granitoid or '
            # result = result + 'Granodiorite'
        
        
    
        
    #if plag < 
    
col1.success("The rock can be classified as: {}".format(result))

#result = ' '
#-------------------------------------------------------
#st.success(result)



# def load_data(uploaded_file):
    # if uploaded_file is not None:
        # try:
            # bytes_data = uploaded_file.read()
            # str_io = StringIO(bytes_data.decode('Windows-1252'))
            # las_file = lasio.read(str_io)
            # well_data = las_file.df()
            # well_data['DEPTH'] = well_data.index

        # except UnicodeDecodeError as e:
            # st.error(f"error loading log.las: {e}")
    # else:
        # las_file = None
        # well_data = None

    # return las_file, well_data


# #TODO
# def missing_data():
    # st.title('Missing Data')
    # missing_data = well_data.copy()
    # missing = px.area(well_data, x='DEPTH', y='DT')
    # st.plotly_chart(missing)

# # Sidebar Options & File Uplaod
# las_file=None
# st.sidebar.write('# LAS Data Explorer')
# st.sidebar.write('To begin using the app, load your LAS file using the file upload option below.')

# uploadedfile = st.sidebar.file_uploader(' ', type=['.las'])
# las_file, well_data = load_data(uploadedfile)

# if las_file:
    # st.sidebar.success('File Uploaded Successfully')
    # st.sidebar.write(f'<b>Well Name</b>: {las_file.well.WELL.value}',unsafe_allow_html=True)
