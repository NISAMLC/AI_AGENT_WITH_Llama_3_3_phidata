from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

load_dotenv()

def get_company_name(company: str)-> str:
    symbols = {
        'State bank of India':'SBIN',
        'Oil & Natural Gas Corporation Limited':'ONGC',
        'INFOSYS':'INFY',
        'Bharat Electronics Limited':'BEL',
        'Hindalco Industries Limited':'HINDALCO'
    }

    return symbols.get(company,"Unknown")

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True),get_company_name], #add our tools here
    show_tool_calls=True,
    markdown = True,
    instructions = ['Use tables to display data']
)

# agent.print_response("write 2 sentence poem about love")
# agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA AND NVDA and show the current price comparison of TSLA with top 5 gainers of last week with their name")
agent.print_response("Compare INFY with RELIANCE.NS in performance and Fundamentals")