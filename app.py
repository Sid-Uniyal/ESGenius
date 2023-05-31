import streamlit as st

# Set the page title
st.title("My Streamlit App")

# Add a heading
st.header("Welcome to my app!")

# Add some text
st.write("This is a Streamlit app example.")

# Add more content
st.subheader("Here are some key points:")
st.markdown("- Point 1")
st.markdown("- Point 2")
st.markdown("- Point 3")

# Display an image
st.image("image.jpg", caption="Image Caption", use_column_width=True)

# Show a dataframe
import pandas as pd
data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.dataframe(df)

# Render a plot
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
st.pyplot(plt)

# Add a footer
st.footer("Thank you for using my app!")