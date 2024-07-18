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
    
    return future_value, future_value_initial_capital, future_value_monthly_investments

# Streamlit app
st.title('📈Monthly Investment Calculator with Initial Capital📈')

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
    future_value, future_value_initial_capital, future_value_monthly_investments = calculate_future_value(initial_capital, monthly_investment, annual_rate, years)
    total_invested = initial_capital + monthly_investment * 12 * years
    total_interest_earned = future_value - total_invested
    st.write(f'After {years} years, with an initial capital of {initial_capital:.2f} € and investing {monthly_investment:.2f} € each month at an annual interest rate of {annual_rate * 100:.2f} %, the final amount will be approximately {future_value:.2f} €.')
    st.write(f'Total interest earned will be approximately {total_interest_earned:.2f} €.')

# Custom CSS for positioning text
custom_css = """
<style>
.bottom-right {
    position: fixed;
    bottom: 10px;
    right: 80px;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
"""

# Custom HTML for the text
custom_html = """
<div class="bottom-right">
    © 2024 Nikolai ROPA
</div>
"""

# Injecting CSS and HTML into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(custom_html, unsafe_allow_html=True)

