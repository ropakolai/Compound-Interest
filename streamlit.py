import streamlit as st
import plotly.graph_objects as go

def calculate_future_value_over_time(initial_capital, monthly_investment, annual_rate, years):
    monthly_rate = annual_rate / 12
    periods = years * 12

    future_values = []
    interests_earned = []
    
    for period in range(1, periods + 1):
        future_value_initial_capital = initial_capital * ((1 + monthly_rate) ** period)
        future_value_monthly_investments = monthly_investment * (((1 + monthly_rate) ** period - 1) / monthly_rate)
        future_value = future_value_initial_capital + future_value_monthly_investments
        
        total_invested = initial_capital + monthly_investment * period
        interest_earned = future_value - total_invested
        
        if period % 12 == 0:  # Capture the value at the end of each year
            future_values.append(future_value)
            interests_earned.append(interest_earned)
    
    return future_values, interests_earned

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
    future_values, interests_earned = calculate_future_value_over_time(initial_capital, monthly_investment, annual_rate, years)
    total_invested = initial_capital + monthly_investment * 12 * years
    future_value = future_values[-1]
    total_interest_earned = future_value - total_invested
    
    st.write(f'After {years} years, with an initial capital of {initial_capital:.2f} € and investing {monthly_investment:.2f} € each month at an annual interest rate of {annual_rate * 100:.2f} %, the final amount will be approximately **{future_value:.2f} €**.')
    st.write(f'Total interest earned will be approximately **{total_interest_earned:.2f} €**.')
    
    # Plotting the future values and interests earned with Plotly
    years_range = list(range(1, years + 1))
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years_range,
        y=future_values,
        mode='lines',
        name='Future Value',
        fill='tonexty',
        fillcolor='rgba(0, 100, 255, 0.2)',
        line=dict(color='blue')
    ))
    
    fig.add_trace(go.Scatter(
        x=years_range,
        y=interests_earned,
        mode='lines',
        name='Total Interest Earned',
        fill='tozeroy',
        fillcolor='rgba(0, 255, 0, 0.2)',
        line=dict(color='green')
    ))
    
    fig.update_layout(
        title='Future Value and Total Interest Earned Over Time',
        xaxis_title='Years',
        yaxis_title='Amount (€)',
        legend_title='Legend',
        template='plotly_white'
    )
    
    st.plotly_chart(fig)

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
