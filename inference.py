import streamlit as st
import pandas as pd
import pickle

def preprocessing_pipeline(df):
    #convert date to datetime
    df['ds']=pd.to_datetime(df['ds'])
    df['ds']=df['ds'].dt.to_period('M')
    df['ds']=df['ds'].dt.to_timestamp()
    return df

def load_model(category):
    with open(f'model/{category}_model.pkl', 'rb') as file:
        model, features = pickle.load(file)
    return model, features

def app():
    st.title('Sales Volume Forecasting')
    st.write('Select the Category of Product to make Prediction')
    category=st.selectbox('Category', ['Accessories', 'Laptop', 'Smartphone', 'Tablet'])
    start_date= st.date_input('Start Date')
    end_date= st.date_input('End Date')

    df=pd.DataFrame({'ds':pd.date_range(start_date, end_date)})

    df=preprocessing_pipeline(df)

    model, features=load_model(category)

    prediction = model.predict(df)

    predict_plot= prediction[['ds', 'yhat']]
    st.line_chart(predict_plot, x= 'ds', y= 'yhat')

if __name__== '__main__':
    app()



