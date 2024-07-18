import streamlit as st

def calculate_future_value(initial_capital, monthly_investment, annual_rate, years):
    # Convert annual rate to a monthly rate
    monthly_rate = annual_rate / 12
    # Total number of periods (months)
    periods = years * 12
    
    # Future value of the initial capital
    future_value_initial_capital = initial_capital * ((1 + monthly_rate) ** periods)
    
    # Future value formula for regular monthly investments
    future_value_monthly_investments = monthly_investment * (((1 + monthly_rate) ** periods - 1) / monthly_rate)
    
    # Total future value
    future_value = future_value_initial_capital + future_value_monthly_investments
    
    return future_value

# Streamlit app
st.title('📈 Monthly Investment Calculator with Initial Capital 📈')

# Brief description
st.write("""
This calculator helps you determine the future value of your investments by considering both an initial capital and regular monthly contributions. 
Compound interest means that the interest you earn each period is added to your principal, so your balance doesn't merely grow, it grows at an accelerating rate.
""")

# User inputs
initial_capital = st.number_input('Initial Capital (€)', min_value=0.0, value=1000.0)
monthly_investment = st.number_input('Monthly Investment (€)', min_value=0.0, value=100.0)
annual_rate = st.number_input('Annual Interest Rate (%)', min_value=0.0, value=5.0) / 100
years = st.number_input('Investment Duration (years)', min_value=0, value=3)

# Calculate future value
if st.button('Calculate'):
    future_value = calculate_future_value(initial_capital, monthly_investment, annual_rate, years)
    st.write(f'After {years} years, with an initial capital of {initial_capital} € and investing {monthly_investment} € each month at an annual interest rate of {annual_rate * 100} %, the final amount will be approximately {future_value:.2f} €.')
