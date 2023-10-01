import streamlit as st
import time

# Create a loading animation function
def loading_animation():
    st.title("AI Assistant Lara - Loading...")
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f"Generating AI Assistant Lara... {i+1}%")
        bar.progress(i + 1)
        time.sleep(0.05)  # Simulate loading time

    st.success("AI Assistant Lara has been generated!")
    st.balloons()

# Display the loading animation
loading_animation()

# Now you can perform tasks with AI assistant Lara after it's generated
st.write("You can now interact with AI Assistant Lara.")