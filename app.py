# %%writefile app.py

from tensorflow.keras.models import load_model  
import streamlit as st 
import numpy as np
import pandas as pd
import base64

first_model = "first_model.h5"
second_model = "second_model.h5"
final_model = "final_model.h5"



def teachable_machine_classification(df, weights_file):
     # Load the model
    model = load_model(weights_file)
    test = model.predict(df)
    test = np.array(test)
    test_df = pd.DataFrame(test)
    st.write(test_df.head(5))
    return test_df

def main():
    
    page = st.sidebar.selectbox("Choose Satellite Navigation Systems", ['Home page' , 'Telemetry Electronics', 'Steering Control' ,'Thrust control'])

    if page == 'Home page': 
        
        home_page()

    elif page == 'Telemetry Electronics':
        Telemetry_Electronics()


    elif page == 'Steering Control':
        Steering_Control()


    else:
        Thrust_control()
   
  



def home_page():
    
    st.markdown("<h1 style='text-align: center; color: blue;'>Assembly Line production optimization</h1>", unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.xavor.com/wp-content/uploads/3-Intelligent-Manufacturing.jpg")
    }

    </style>
    """,
    unsafe_allow_html=True
    )
def Telemetry_Electronics():
    st.markdown("<h1 style='text-align: center; color: black;'>Telemetry Electronics</h1>", unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://th.bing.com/th/id/R3c363a11aecebd7e76f18f23f81e5c2e?rik=xBXL%2bdFNrjtLSA&riu=http%3a%2f%2fwallpapercave.com%2fwp%2fCy7YPNg.jpg&ehk=QtoG1zotzCDq%2beIQ7SHA6xKvIQZaZGm13fK7HoOLxXA%3d&risl=&pid=ImgRaw")
    }

    </style>
    """,
    unsafe_allow_html=True
    )

    left_column , middle_column , right_column , last_column = st.beta_columns(4)
    # You can use a column just like st.sidebar:
    left_column.button('Robot number' , key = 1)

    # Or even better, call Streamlit functions inside a "with" block:
    with left_column:
        chosen_machine1 = st.radio(
            'Robot number',
            ("Robot A", "Robot B" ,"Robot C") , key = 2)
        st.write(f"You Choose   {chosen_machine1} ")


    middle_column.button('choose Robot number' , key = 3)

    # Or even better, call Streamlit functions inside a "with" block:
    with middle_column:
        chosen_machine2 = st.radio(
            'Robot number',
            ("Robot A", "Robot B" ,"Robot C") , key = 4)
        st.write(f"You Choose   {chosen_machine2} ")        


    right_column.button('choose Robot number' , key = 23)
    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen_machine21 = st.radio(
            'Robot number',
            ("Robot A", "Robot B" ,"Robot C") , key = 24)
        st.write(f"You Choose  {chosen_machine21} ") 
        
    last_column.button('choose connection Between Robot' ,key = 5)
    # Or even better, call Streamlit functions inside a "with" block:
    with last_column:

        chosen_kind1 = st.radio(
            'Robot number',
            ("Parallel" , ) , key = 14)
        st.write(f"Robot connection {chosen_kind1} ")   
    st.markdown("<h1 style='text-align: right; color: black;'> Upload Features For The Robot in The Telemetry Electronics component </h1>", unsafe_allow_html=True)
    fileTypes = ["csv"]
    file = st.file_uploader("", type=fileTypes)
    download_file = st.button("download output file")
    if file is not None:
        df = pd.read_csv(file)
        if df.shape[1] != 41:
            st.error("input shape is not correct ")
        else:    
            df = df.iloc[: , :41]
            st.write("predict...")
            output_df_Telemetry_Electronics = teachable_machine_classification(df, first_model)
            if download_file == True:
                csv = output_df_Telemetry_Electronics.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()  # some strings
                linko= f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download output file</a>'
                st.markdown(linko, unsafe_allow_html=True)


def Steering_Control():  
    st.markdown("<h1 style='text-align: center; color: black;'> Steering Control </h1>", unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://th.bing.com/th/id/R3c363a11aecebd7e76f18f23f81e5c2e?rik=xBXL%2bdFNrjtLSA&riu=http%3a%2f%2fwallpapercave.com%2fwp%2fCy7YPNg.jpg&ehk=QtoG1zotzCDq%2beIQ7SHA6xKvIQZaZGm13fK7HoOLxXA%3d&risl=&pid=ImgRaw")
    }

    </style>
    """,
    unsafe_allow_html=True
    )

    left_column , middle_column , right_column = st.beta_columns(3)
    # You can use a column just like st.sidebar:

    left_column.button('choose Robot number' , key = 11)

    # Or even better, call Streamlit functions inside a "with" block:
    with left_column:
        
        chosen_machine3 = st.radio(
            'Robot number',
            ("Robot D", "Robot E") , key = 21)
        st.write(f"You Choose  {chosen_machine3} ")


    middle_column.button('choose Robot number' , key = 31)

    # Or even better, call Streamlit functions inside a "with" block:
    with middle_column:
        
        chosen_machine4 = st.radio(
            'Robot number',
            ( "Robot D", "Robot E") , key = 41)
        st.write(f"You Choose   {chosen_machine4} ")        

    right_column.button('choose connection Between Robots' ,key = 51)

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen_kind2 = st.radio(
            'Robot number',
            ("Series", "Parallel") , key =31 )
        st.write(f"You Choose Robot {chosen_kind2} ")   

    st.markdown("<h1 style='text-align: right; color: black;'> Upload Features For The machines in The Steering Control component </h1>", unsafe_allow_html=True)

    fileTypes = ["csv"]

    file2 = st.file_uploader("", type=fileTypes ,key=1)
    download_file = st.button("download output file")
    if file2 is not None:
        df = pd.read_csv(file2)
        if df.shape[1] != 16:
            st.error("input shape is not correct ")
        else:    
            df = df.iloc[: , :16]
            st.write("predict...")
            output_df = teachable_machine_classification(df, second_model)
            if download_file == True:
                csv = output_df.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()  # some strings
                linko= f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download output file</a>'
                st.markdown(linko, unsafe_allow_html=True)

 
def Thrust_control():
    

    st.markdown("<h1 style='text-align: center; color: black;'> Thrust control </h1>", unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://th.bing.com/th/id/R3c363a11aecebd7e76f18f23f81e5c2e?rik=xBXL%2bdFNrjtLSA&riu=http%3a%2f%2fwallpapercave.com%2fwp%2fCy7YPNg.jpg&ehk=QtoG1zotzCDq%2beIQ7SHA6xKvIQZaZGm13fK7HoOLxXA%3d&risl=&pid=ImgRaw")
    }

    </style>
    """,
    unsafe_allow_html=True
    )

    left_column , middle_column , right_column = st.beta_columns(3)
    # You can use a column just like st.sidebar:

    left_column.button('choose Robot number' , key = 101)

    # Or even better, call Streamlit functions inside a "with" block:
    with left_column:
        
        chosen_machine3 = st.radio(
            'Robot number',
            ("Robot F", "Robot G") , key = 21)
        st.write(f"You Choose  {chosen_machine3} ")


    middle_column.button('choose Robot number' , key = 301)

    # Or even better, call Streamlit functions inside a "with" block:
    with middle_column:
        chosen_machine4 = st.radio(
            'Robot number',
            ( "Robot F", "Robot G") , key = 41)
        st.write(f"You Choose {chosen_machine4} ")        

    right_column.button('choose Robot number' ,key = 501)

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen_kind2 = st.radio(
            'Robot number',
            ("Series", "Parallel") , key =331 )
        st.write(f"You Choose Robot to be  {chosen_kind2} ")   

    st.markdown("<h1 style='text-align: right; color: black;'> Upload Features For The machines in The Thrust control component </h1>", unsafe_allow_html=True)

    fileTypes = ["csv"]

    file2 = st.file_uploader("", type=fileTypes ,key=61)
    download_file = st.button("download output file")
    if file2 is not None:

        df = pd.read_csv(file2)
        if df.shape[1] != 25:
            st.error("input shape is not correct ")
        else:    
            df = df.iloc[: , :25]
            st.write("predict...")
            output_df = teachable_machine_classification(df, final_model)
            if download_file == True:
                csv = output_df.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()  # some strings
                linko= f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download output file</a>'
                st.markdown(linko, unsafe_allow_html=True)

    


if __name__ == "__main__":
   
    main()
