import streamlit as st

# Conversion factors
length_units = {
    'meter': 1,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.344
}

weight_units = {
    'kilogram': 1,
    'gram': 0.001,
    'milligram': 0.000001,
    'pound': 0.453592,
    'ounce': 0.0283495,
    'ton': 1000
}

volume_units = {
    'liter': 1,
    'milliliter': 0.001,
    'gallon': 3.78541,
    'quart': 0.946353,
    'pint': 0.473176,
    'cup': 0.24,
    'fluid ounce': 0.0295735
}

temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']

# Function for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return value * 9/5 + 32
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return value

st.title("🔄 Unit Converter")
st.markdown("Convert between various unit types in real-time")

# Category selection
category = st.selectbox("Select category:", ['Length', 'Weight', 'Volume', 'Temperature'])

# Assign correct unit dictionary
if category == 'Length':
    units = length_units
elif category == 'Weight':
    units = weight_units
elif category == 'Volume':
    units = volume_units
else:
    units = temperature_units

col1, col2, col3 = st.columns([2, 2, 3])
with col1:
    from_unit = st.selectbox("From unit:", options=list(units.keys()) if category != 'Temperature' else temperature_units)
with col2:
    to_unit = st.selectbox("To unit:", options=list(units.keys()) if category != 'Temperature' else temperature_units)

value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0, step=0.1, format="%.4f")

# Conversion
if category == 'Temperature':
    result = convert_temperature(value, from_unit, to_unit)
else:
    if from_unit == to_unit:
        result = value
    else:
        in_base = value * units[from_unit]
        result = in_base / units[to_unit]

st.markdown(f"**Converted value:** `{value:,.4f} {from_unit} = {result:,.4f} {to_unit}`")


# How to run instructions in sidebar
st.sidebar.markdown("### How to Use")
st.sidebar.markdown("""
1. Select the input unit (FROM)
2. Select the output unit (TO)
3. Enter the value to convert
4. View instant results and conversion details
""")
st.sidebar.write("Design By: ATIQ SARWAR")