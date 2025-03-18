import streamlit as st
import pint

# Initialize Pint unit registry
ureg = pint.UnitRegistry()

# Streamlit UI
st.title("Unit Converter" )

st.markdown(
    """
    <style>
        body {
            background-color: #EEC643;
            color: white;
        }
        .stApp {
            background-color: #99f2c8;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #011638;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            background-color: #EEC643;
            color: black;
            font-size: 18px;
            text-align: center;
        }
        .st.selectbox {
            background-color: #;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define unit categories
categories = {
    "Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "cup"],
}

# Select category
category = st.selectbox("Select a category:", list(categories.keys()))




# Select units
from_unit = st.selectbox("From:", categories[category])
to_unit = st.selectbox("To:", categories[category])




# Input value
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")




# Conversion logic
if st.button("Convert"):



    try:
        # Convert units using Pint
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.2f} {to_unit}")




    except Exception as e:
        st.error(f"Conversion error: {e}")
