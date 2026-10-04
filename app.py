import streamlit as st


def calculate(a, b, op):
    if op == "Addition (+)":
        return a + b
    if op == "Subtraction (-)":
        return a - b
    if op == "Multiplication (*)":
        return a * b
    if op == "Division (/)":
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero.")
        return a / b
    if op == "Power (^)":
        return a ** b
    if op == "Modulus (%)":
        if b == 0:
            raise ZeroDivisionError("Modulus by zero is not allowed.")
        return a % b
    raise ValueError("Unknown operation")


st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
st.title("Simple Calculator")

col1, col2 = st.columns(2)
a = col1.number_input("First number", value=0.0, format="%f")
b = col2.number_input("Second number", value=0.0, format="%f")

operation = st.selectbox(
    "Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
        "Power (^)",
        "Modulus (%)",
    ],
)

if st.button("Calculate"):
    try:
        result = calculate(a, b, operation)
        st.success(f"Result: {result}")
    except ZeroDivisionError as e:
        st.error(str(e))
    except OverflowError:
        st.error("That number is too big to handle.")
