import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

# Set page title
st.title("3D Visualization of a Cone")

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
height = st.number_input("Height (h) in mm", min_value=0.0, value=2.0, step=0.1)

# Calculate volume and show 3D plot
if radius > 0 and height > 0:
    # Calculate volume
    volume = (1/3) * math.pi * (radius ** 2) * height
    
    # Display result
    st.header("Result")
    st.success(f"Volume of the cone is: {volume:.2f} mm$^3$")
    
    # Create 3D visualization
    st.header("3D Visualization")
    
    # Generate cone coordinates
    theta = np.linspace(0, 2 * np.pi, 50)
    z = np.linspace(0, height, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    
    x = (radius / height) * (height - z_grid) * np.cos(theta_grid)
    y = (radius / height) * (height - z_grid) * np.sin(theta_grid)
    
    # Create 3D surface plot
    fig = go.Figure(data=[go.Surface(
        x=x, 
        y=y, 
        z=z_grid,
        colorscale='Blues',
        showscale=False
    )])
    
    # Configure plot layout
    fig.update_layout(
        scene=dict(
            xaxis_title='X (Radius)',
            yaxis_title='Y (Radius)',
            zaxis_title='Z (Height)',
            camera=dict(eye=dict(x=1.5, y=1.5, z=0.8)),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=0.7)
        ),
        margin=dict(l=0, r=0, b=0, t=30),
        height=500
    )
    
    # Display plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
else:
    st.warning("Please enter positive values for radius and height")
