from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('logistic')

def predict_churn(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['Label'][0]
    

st.title('Customer Churn Web App')
st.write('This is a web app to classify whether a customer will churn based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction of the classifier.')


def run():

    from PIL import Image
    image_2 = Image.open('churn_image.jpeg')

    #st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.image(image_2)

    st.sidebar.info('This app is created to predict if a customer will churn')
    st.sidebar.success('https://www.github.com/pereira94')
    
    if add_selectbox == 'Online':

        tenure = st.number_input('Tenure in Months', min_value=0, max_value=80, value=7)
        MonthlyCharges = st.number_input('Monthly Charges', min_value=18, max_value=119, value=65)
        gender = st.selectbox('Gender', ['Male', 'Female'])
        MultipleLines = st.selectbox('Multiple lines?', ['No', 'Yes', 'No phone service'])
        InternetService = st.selectbox('Internet Service?', ['Fiber optic', 'DSL', 'No'])
        OnlineSecurity = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
        OnlineBackup = st.selectbox('Online Backup?', ['No', 'Yes', 'No internet service'])
        DeviceProtection = st.selectbox('Device Protection?', ['No', 'Yes', 'No internet service'])
        TechSupport = st.selectbox('Tech Support?', ['No', 'Yes', 'No internet service'])
        StreamingTV = st.selectbox('Streaming TV?', ['No', 'Yes', 'No internet service'])
        StreamingMovies = st.selectbox('Streaming Movies?', ['No', 'Yes', 'No internet service'])
        Contract = st.selectbox('Contract?', ['Month-to-month', 'Two year', 'No internet service'])
        PaymentMethod = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 
        'Bank transfer (automatic)', 'Credit card (automatic)'])


        if st.checkbox('Senior Citizen?'):
            SeniorCitizen = 1
        else:
            SeniorCitizen = 0

        if st.checkbox('Has Partner?'):
            Partner = True
        else:
            Partner = False
        
        if st.checkbox('Has Dependents?'):
            Dependents = True
        else:
            Dependents = False

        if st.checkbox('Has Phone Service?'):
            PhoneService = True
        else:
            PhoneService = False

        if st.checkbox('Paperless Billing?'):
            PaperlessBilling = True
        else:
            PaperlessBilling = False
        
        output=""

        input_dict = {'tenure' : tenure, 'MonthlyCharges' : MonthlyCharges, 'gender' : gender, 'MultipleLines' : MultipleLines, 
        'InternetService' : InternetService, 'OnlineSecurity' : OnlineSecurity, 'OnlineBackup' : OnlineBackup,
        'DeviceProtection' : DeviceProtection, 'TechSupport': TechSupport, 'StreamingTV': StreamingTV,
        'StreamingMovies' : StreamingMovies, 'Contract':Contract, 'PaymentMethod' : PaymentMethod,
        'SeniorCitizen' : SeniorCitizen, 'Partner' : Partner, 'Dependents' : Dependents, 'PhoneService':PhoneService, 'PaperlessBilling' : PaperlessBilling}
        df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict_churn(model=model, df=df)

        st.success('Will the customer leave? {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()