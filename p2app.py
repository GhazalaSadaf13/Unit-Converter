import streamlit as st

# Dictionary
conversion_factor={
    "denier":1,
    "tex":9/1,
    "english cotton count (Ne)":5315/1,
    "metric":10000/1,
    "woolen":3000/1
}

# Function to convert Denier to Tex
def denier_to_tex(denier):
    return denier * 0.1111

# Streamlit UI
st.title("Textile Count Converter")
st.header("Convert Denier to Tex")

# Input field for Denier
denier_value = st.number_input("Enter Denier value:", min_value=0.0, format="%.2f")

# Convert and display result
if st.button("Convert"):
    tex_value = denier_to_tex(denier_value)
    st.success(f"{denier_value} Denier is equal to {tex_value:.4f} Tex")

#Reset for another
if st.button("Reset"):
    st.experimental_rerun()