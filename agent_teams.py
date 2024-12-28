from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

load_dotenv()


web_Agent = Agent(
    name = 'web agent',
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()], #add our tools here
    instructions = ['always include sources'],
    show_tool_calls=True,
    markdown = True,

)




fin_agent = Agent(
    name = "fin_agent",
    role='Get financial data',
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)], #add our tools here
    instructions = ['Use tables to display data'],
    show_tool_calls=True,
    markdown = True,

)

agent_team = Agent(
    team = [web_Agent,fin_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources",'Use tables to display data'],
    show_tool_calls=True,
    markdown=True,

)


# agent.print_response("write 2 sentence poem about love")
# agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA AND NVDA and show the current price comparison of TSLA with top 5 gainers of last week with their name")
agent_team.print_response("Summarize analyst recommendations and share the latest news for INFY")