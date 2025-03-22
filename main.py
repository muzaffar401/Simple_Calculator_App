import streamlit as st
import math

def main():
    # Page Configuration
    st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")
    
    # Title
    st.title("🧮 Advanced Calculator")
    st.write("Perform basic and advanced mathematical operations!")
    
    # Operation Selection
    operation = st.selectbox(
        "Choose operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (^)", "Square Root (√)", "Modulus (%)"]
    )
    
    # Input Fields (Conditional Display)
    if operation in ["Square Root (√)", "Power (^)"]:
        num1 = st.number_input("Enter number", value=0.0, key="num1")
        num2 = None if operation == "Square Root (√)" else st.number_input("Enter exponent", value=0.0, key="num2")
    else:
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Enter first number", value=0.0, key="num1")
        with col2:
            num2 = st.number_input("Enter second number", value=0.0, key="num2")
    
    # Calculate Button
    if st.button("Calculate 🚀"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            elif operation == "Division (÷)":
                if num2 == 0:
                    st.error("❌ Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"
            elif operation == "Power (^)":
                result = num1 ** num2
                symbol = "^"
            elif operation == "Square Root (√)":
                if num1 < 0:
                    st.error("❌ Error: Cannot calculate square root of a negative number!")
                    return
                result = math.sqrt(num1)
                symbol = "√"
            else:  # Modulus
                result = num1 % num2
                symbol = "%"
            
            # Store Calculation History
            if "history" not in st.session_state:
                st.session_state.history = []
            history_entry = f"{num1} {symbol} {num2 if num2 is not None else ''} = {result}"
            st.session_state.history.append(history_entry)
            
            # Display Result
            st.success(f"✅ Result: {history_entry}")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")
    
    # Show Calculation History
    if "history" in st.session_state and st.session_state.history:
        st.subheader("📜 Calculation History")
        for calc in st.session_state.history[-5:]:  # Show last 5 calculations
            st.write(calc)

# Run the app
if __name__ == "__main__":
    main()
