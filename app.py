import streamlit as st
import time
import subprocess

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('ESGenius/esg-background.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the page title
st.title("Welcome to ESGenius")

# Add a heading
#st.header("Welcome to my app!")

# Function to simulate a long-running process
def simulate_processing():
    # Add a delay to simulate processing
    time.sleep(3)
    
#def run_python_file(file_path):
#    result = subprocess.run(["python", file_path], capture_output=True, text=True)
#    output = result.stdout.strip()
#    return output
    
# Add some text
st.write("ESGenius app will give you the methods to control your organizations carbon emissions. Please click the Generate button below to proceed")
if st.button("Generate"):
    # Display a spinner while processing
    with st.spinner("Processing..."):
        output = subprocess.run(["python", "ESGenius/genai_core_engine.py"], capture_output=True, text=True)
        simulate_processing()
        st.success("Processing completed")
        st.code(output, language="python")
        

# Add more content
#st.subheader("Here are some key points:")
#st.markdown("- Point 1")
#st.markdown("- Point 2")
#st.markdown("- Point 3")
#output="Output from LLM will come here"
#st.write(output)

# Display an image
#st.image("image.jpg", caption="Image Caption", use_column_width=True)

# Show a dataframe
#import pandas as pd
#data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35]}
#df = pd.DataFrame(data)
#st.dataframe(df)

# Render a plot
#import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
#st.pyplot(plt)

# Add a footer
#st.footer("Thank you for using my app!")