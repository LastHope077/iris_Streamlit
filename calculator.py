import streamlit as st

st.title('Simple Calculator App')
st.write('Perform basic arithmetic operations')

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input('Enter first number:', value=0.0)

with col2:
    num2 = st.number_input('Enter second number:', value=0.0)

# Operation selector
operation = st.selectbox('Select operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Calculate button
if st.button('Calculate'):
    result = None
    
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 == 0:
            st.error('Cannot divide by zero!')
        else:
            result = num1 / num2
    
    if result is not None:
        st.success(f'Result: {num1} {operation.lower()} {num2} = {result}')