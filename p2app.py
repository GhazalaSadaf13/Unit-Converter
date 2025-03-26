import streamlit as st

# Dictionary for conversion factors
conversion_factor = {
    "Denier": 1,
    "Tex": 9,
    "English Cotton Count (Ne)": 5315,
    "Metric": 10000,
    "Woolen": 3000
}

# Function to convert between textile counts
def convert_count(value, from_unit, to_unit):
    if from_unit in conversion_factor and to_unit in conversion_factor:
        return value * (conversion_factor[to_unit] / conversion_factor[from_unit])
    else:
        return None

# Streamlit UI
st.title("🧵 Textile Count Converter")
st.header("Convert Between Different Yarn Count Systems")

# Input field for value
count_value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Dropdowns to select units
from_unit = st.selectbox("Convert from:", list(conversion_factor.keys()))
to_unit = st.selectbox("Convert to:", list(conversion_factor.keys()))

# Convert and display result
if st.button("Convert"):
    if from_unit == to_unit:
        st.warning("⚠️ Please select different units to convert!")
    else:
        result = convert_count(count_value, from_unit, to_unit)
        if result is not None:
            st.success(f"{count_value:.2f} {from_unit} is equal to {result:.4f} {to_unit}")
        else:
            st.error("❌ Conversion failed. Please check the values and try again.")

# Reset button to clear inputs
if st.button("Reset"):
    st.experimental_rerun()
