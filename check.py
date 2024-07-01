import streamlit as st
from currency_converter import CurrencyConverter

def currency_converter():
    st.title("Currency Converter")

    # Get the amount to convert
    amount = st.number_input("Enter the amount to convert", min_value=0.01, step=0.01)

    # List of supported currencies for the specified countries
    supported_currencies = ["USD", "INR", "GBP", "EUR", "CAD", "BRL", "AUD", "JPY", "SEK", "PLN", "LKR"]

    # Select the target currency
    target_currency = st.selectbox("Select target currency", options=supported_currencies)

    # Fetch the latest exchange rate
    exchange_rate = fetch_exchange_rate("USD", target_currency)

    if exchange_rate:
        # Perform the currency conversion
        result = amount * exchange_rate

        # Display the result
        st.success(f"{amount} USD is approximately {result:.2f} {target_currency}")
    else:
        st.error("Error fetching exchange rate. Please try again later.")
    calculator()

def fetch_exchange_rate(source_currency, target_currency):
    c = CurrencyConverter()
    try:
        if target_currency == "LKR":
            # Manually specify the exchange rate for USD to LKR conversion
            return 298.00
        else:
            # Get the exchange rate using the currency_converter library
            exchange_rate = c.convert(1, source_currency, target_currency)
            return exchange_rate
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

def calculator():
    st.title("Calculator")

    # Get user input for first number
    num1 = st.number_input("Enter first number")

    # Get user input for operation
    operation = st.selectbox("Select operation", ["+", "-", "*", "/"])

    # Get user input for second number
    num2 = st.number_input("Enter second number")

    # Perform calculation based on operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    # Display the result
    st.success(f"Result: {result}")

if __name__ == "__main__":
    currency_converter()
    calculator()
