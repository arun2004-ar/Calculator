import streamlit as st

# Title for the app
st.title("Simple Calculator??????????????????")

# User input for numbers
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Dropdown for operation selection
operation = st.selectbox(
    "Select an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Perform calculation based on the operation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Division by zero is not allowed!")

# Display the result
if result is not None:
    st.success(f"The result is: {result}")
