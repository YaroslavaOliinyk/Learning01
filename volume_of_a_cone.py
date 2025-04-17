import streamlit as st
import math

# Set page title
st.title("Calculation of the Volume of a Cone")

# Display formula explanation
st.header("Formula")
st.latex(r"Volume = \frac{1}{3} \pi r^2 h")
st.write("where:")
st.write("- π (pi) is approximately 3.14159")
st.write("- r is the radius of the base")
st.write("- h is the height of the cone")

# Input fields
st.header("Input Values")
radius = st.number_input("Radius (r) in mm", min_value=0.0, value=1.0, step=0.1)
height = st.number_input("Height (h) in mm", min_value=0.0, value=1.0, step=0.1)

# Calculate volume
if radius > 0 and height > 0:
    volume = (1/3) * math.pi * (radius ** 2) * height
    st.header("Result")
    st.success(f"Volume of the cone is: {volume:.2f} mm$^3$")
else:
    st.warning("Please enter positive values for radius and height")
