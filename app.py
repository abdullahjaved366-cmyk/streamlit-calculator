import time

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
        result = a ** b
        if isinstance(result, complex):
            raise ValueError("That power doesn't give a real number.")
        return result
    if op == "Modulus (%)":
        if b == 0:
            raise ZeroDivisionError("Modulus by zero is not allowed.")
        return a % b
    raise ValueError("Unknown operation")


def fmt(x):
    """Whole numbers show as integers, everything else gets exactly 2 decimals."""
    if abs(x) >= 1e15:
        return f"{x:.2e}"
    if round(x, 2) == int(round(x, 2)):
        return f"{int(round(x, 2)):,}"
    return f"{x:,.2f}"


def fmt_time(seconds):
    ms = seconds * 1000
    if ms < 1:
        return f"{seconds * 1_000_000:.2f} µs"
    return f"{ms:.2f} ms"


SYMBOLS = {
    "Addition (+)": "+",
    "Subtraction (-)": "-",
    "Multiplication (*)": "×",
    "Division (/)": "÷",
    "Power (^)": "^",
    "Modulus (%)": "%",
}


st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
st.title("🧮 Simple Calculator")
st.caption("Pick two numbers and an operation. Results are rounded to 2 decimals.")

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns(2)
a = col1.number_input("First number", value=0.0, step=1.0, format="%g")
b = col2.number_input("Second number", value=0.0, step=1.0, format="%g")

operation = st.selectbox("Operation", list(SYMBOLS.keys()))

if st.button("Calculate", type="primary"):
    try:
        start = time.perf_counter()
        result = calculate(a, b, operation)
        elapsed = time.perf_counter() - start

        expression = f"{fmt(a)} {SYMBOLS[operation]} {fmt(b)} = {fmt(result)}"
        st.success(f"Result: {fmt(result)}")
        st.caption(f"⏱ Executed in {fmt_time(elapsed)}")

        st.session_state.history.insert(0, expression)
        st.session_state.history = st.session_state.history[:5]
    except ZeroDivisionError as e:
        st.error(str(e))
    except ValueError as e:
        st.error(str(e))
    except OverflowError:
        st.error("That number is too big to handle.")

if st.session_state.history:
    st.divider()
    st.subheader("Recent calculations")
    for item in st.session_state.history:
        st.write(item)
    if st.button("Clear history"):
        st.session_state.history = []
        st.rerun()
