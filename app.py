
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analytics")
st.write("Analyze student academic performance using Python.")

st.sidebar.header("Student Information")

name = st.sidebar.text_input("Student Name")

math = st.sidebar.number_input("Math Marks", 0, 100, 75)
english = st.sidebar.number_input("English Marks", 0, 100, 80)
science = st.sidebar.number_input("Science Marks", 0, 100, 85)

if st.button("Analyze Performance"):

    subjects = ["Math", "English", "Science"]
    marks = [math, english, science]

    total = sum(marks)
    average = total / len(marks)
    percentage = (total / 300) * 100

    st.subheader(f"Results for {name or 'Student'}")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Marks", f"{total}/300")
    col2.metric("Average", f"{average:.2f}")
    col3.metric("Percentage", f"{percentage:.2f}%")

    df = pd.DataFrame({
        "Subject": subjects,
        "Marks": marks
    })

    st.subheader("Subject-wise Performance")
    st.bar_chart(df.set_index("Subject"))

    if percentage >= 80:
        st.success("Excellent Performance!")
    elif percentage >= 60:
        st.info("Good Performance!")
    else:
        st.warning("Keep Practicing!")

