import streamlit as st

# Function to calculate budget allocation
def calculate_budget(salary):
    expenses = 0.5 * salary
    wants = 0.2 * salary
    investments = 0.2 * salary
    development = 0.1 * salary
    return expenses, wants, investments, development

# Function to recommend investment portfolio
def recommend_portfolio(amount, goal):
    if goal == 'Short Term':
        debt_funds = amount
        equity_funds = 0
        crypto = 0
        gold = 0
        reits = 0
    elif goal == 'Mid Term':
        debt_funds = 0.7 * amount
        equity_funds = 0.3 * amount
        crypto = 0
        gold = 0
        reits = 0
    else:
        debt_funds = 0.15 * amount
        equity_funds = 0.6 * amount
        crypto = 0.1 * amount
        gold = 0.05 * amount
        reits = 0.05 * amount
    return debt_funds, equity_funds, crypto, gold, reits

def main():

    # Main page content
    st.set_page_config(page_title='munBud - Your finance buddy', page_icon="	:money_mouth_face:",)
    st.title("**munBud** - _Your finance buddy_ :money_mouth_face: ")
    st.write("---")

    # Sidebar options
    option = st.sidebar.selectbox(
        'Select an option:',
        ('Budget Calculator', 'Investment Advisor', 'About'),
    )

    # Add a note to the sidebar
    st.sidebar.write("---")
    st.sidebar.write('''
                        **Note:** Choose your **Risk - Reward** wisely and invest your money **wisely** according to your *goals*.
                        
                        **_Happy Investing_** :heart:
                                                        ''')


    if option == 'Budget Calculator':
        st.write('### Budget Calculator')
        col, buff = st.columns((1, 1))
        with col:
            salary = st.number_input('Enter your monthly salary (e.g:- 500000):',  step=500)

        if salary:
            expenses, wants, investments, development = calculate_budget(salary)
            st.write('### Budget Allocation')
            st.write(f'*50% for* `Expenses`: **₹{expenses:.2f}**')
            st.write(f'*20% for* `Wants`: **₹{wants:.2f}**')
            st.write(f'*20% for* `Investments and Emergency Fund`: **₹{investments:.2f}**')
            st.write(f'*10% for* `Self Development`: **₹{development:.2f}**')

    elif option == 'Investment Advisor':
        st.write('### Investment Advisor')
        col, buff = st.columns((1, 1))
        with col:
            amount = st.number_input('Enter the investment amount: (e.g:- 5000)',  step=500)
            goal = st.selectbox('Select your investment goal:', ('Short Term', 'Mid Term', 'Long Term'))

        if amount and goal:
            st.write("---")
            st.write('#### Recommended Investment Portfolio')
            debt_funds, equity_funds, crypto, gold, reits = recommend_portfolio(amount, goal)
            st.write(f'`Debt Funds`: **₹{debt_funds:.2f}**')
            st.write(f'`Equity Funds`: **₹{equity_funds:.2f}**')
            st.write(f'`Crypto`: **₹{crypto:.2f}**')
            st.write(f'`Gold`: **₹{gold:.2f}**')
            st.write(f'`REITs`: **₹{reits:.2f}**')

    else:
        st.write('### About')
        st.markdown('''
        *munBud* is developed by **Mubarak Mayyeri** (AI developer, Data Scientist, Python Backend developer)

        * Github Repo of munBud - https://github.com/mubarakmayyeri/munbud'
        * Connect me on LinkedIn - https://www.linkedin.com/in/mubarakmayyeri/'

        
        _If you want to contribute or suggest new features use the links provided_. Let\'s work together and achieve our financial goals.
        ''')

if __name__ == "__main__":
    main()