import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Energy Consumption Predictor",
    page_icon="⚡",
    layout="wide"
)

# Background styling
st.markdown("""
<style>
.stApp {
background: linear-gradient(to right, #74ebd5, #ACB6E5);
}

[data-testid="stSidebar"] {
background-color: #2E86C1;
color: white;
}

div.stButton > button {
background-color: #27AE60;
color: white;
font-size: 18px;
border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model/model.pkl","rb"))

# Load dataset
data = pd.read_csv("dataset/energy_data.csv")

# Sidebar
st.sidebar.title("📌 Menu")

option = st.sidebar.selectbox(
    "Select Page",
    ("🏠 Home", "🔍 Prediction", "📊 Data Visualization", "📋 Dataset", "💡 Energy Tips")
)

# Home Page
if option == "🏠 Home":

    st.markdown("<h1 style='text-align:center;color:#1B4F72;'>⚡ Energy Consumption Prediction System</h1>", unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/1048/1048953.png", width=120)

    st.write("""
This system predicts electricity consumption using Machine Learning.
It helps industries and households analyze energy usage and reduce electricity waste.
""")

    st.subheader("📖 Features")

    st.write("""
✔ Energy consumption prediction  
✔ Data visualization graphs  
✔ Dataset preview  
✔ Download prediction results  
✔ Energy saving tips  
""")

# Prediction Page
elif option == "🔍 Prediction":

    st.header("⚡ Predict Energy Consumption")

    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.slider("🌡 Temperature", 0, 50, 25)

    with col2:
        humidity = st.slider("💧 Humidity", 0, 100, 50)

    with col3:
        appliances = st.slider("🔌 Appliances", 1, 10, 3)

    if st.button("⚡ Predict Energy Consumption"):

        prediction = model.predict([[temperature, humidity, appliances]])

        st.success(f"⚡ Predicted Energy Consumption: {prediction[0]:.2f} kWh")

        result = pd.DataFrame({
            "Temperature":[temperature],
            "Humidity":[humidity],
            "Appliances":[appliances],
            "Predicted Energy":[prediction[0]]
        })

        st.download_button(
            label="⬇ Download Result",
            data=result.to_csv(index=False),
            file_name="prediction_result.csv"
        )

# Visualization Page
elif option == "📊 Data Visualization":

    st.subheader("📊 Energy Consumption Graph")

    fig, ax = plt.subplots()

    ax.plot(data['Energy'])

    ax.set_xlabel("Record")

    ax.set_ylabel("Energy Consumption")

    st.pyplot(fig)

# Dataset Page
elif option == "📋 Dataset":

    st.subheader("📋 Dataset Preview")

    st.dataframe(data)

# Energy Tips Page
elif option == "💡 Energy Tips":

    st.subheader("💡 Energy Saving Tips")

    st.write("""
🔌 Turn off unused appliances  
💡 Use LED lights  
🌡 Maintain optimal AC temperature  
🔋 Use energy-efficient appliances  
🏠 Improve insulation to reduce cooling/heating load  
""")

# Footer
st.markdown("---")
st.markdown("⚡ Developed for Energy Consumption Prediction Project")