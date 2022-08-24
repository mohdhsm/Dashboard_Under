
import pandas as pd
import streamlit as st
import datetime
import numpy as np 

# ========= SIDE BAR =====

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)



# Title 
st.title("OKR Sheet")
sales_df = pd.read_excel("data/df_sales.xlsx")
# Selecting the objectives to seperate
obj1 = sales_df[sales_df['Obj']== 1]
obj2 = sales_df[sales_df['Obj']==2]
obj3 = sales_df[sales_df['Obj']== 3]
obj4 = sales_df[sales_df['Obj']== 4]
# STATUS
# When started, make cell red 
def Highlighters(s,bg=" "):
    if (str(s).lower() == "started"):
        bg = "background-color:green;"
    elif((str(s).lower() == "not started")):
        bg = "background-color:sandybrown;"
    elif((str(s).lower() == "stuck")):
        bg = "background-color:red;"
    else:
        bg = " "

    return bg



# Highlight the difference between the current and target
def Highlight_Difference(x):
    m1 = x['Target']>x['Current']
    m2= x['Status'].str.contains("started", na = False, case= False)
    m3 =x['Status'].str.contains("not", na=False, case=False)
    m4 =  x['Status'].str.contains("stuck", na=False, case=False)
# Wrote the style in a styles datafram
    df1 = pd.DataFrame("background-color: ",index = x.index, columns=x.columns)
    df1['Current'] = np.where(m1,"background-color:Indigo;",df1["Current"])
    df1['Status'] = np.where(m2,"background-color:green;",df1["Status"])
    df1['Status'] = np.where(m3,"background-color:sandybrown;",df1["Status"])
    df1['Status'] = np.where(m4,"background-color:red;",df1["Status"])
    # Rewrite booleansj
    return df1

    
# Split the objectives
st.write("OBJ1: Increase sales inside aramco")
st.write(obj1.style.apply(Highlight_Difference,axis=None))

st.write("OBJ2: Increase the profit margin from the deals")
st.write(obj2.style.applymap(Highlighters))

st.write("OBJ3: Our sales people are highly trained")
st.write(obj3.style.applymap(Highlighters))


st.write("OBJ4: increase sales from outside aramco")
st.write(obj4.style.applymap(Highlighters))

# Create the metrics or a different page.

