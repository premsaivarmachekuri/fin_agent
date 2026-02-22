import dspy
from dspy.adapters.types.tool import Tool
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from app.core.langgraph.tools.market_data import get_stock_price, compare_stocks
from app.core.prompts.system import SYSTEM_PROMPT, FINANCIAL_ANALYSIS_SIGNATURE
from app.utils.logger import logger

# Configure DSPy
lm = dspy.LM('ollama_chat/llama3.2', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm, allow_tool_async_sync_conversion=True)

# Convert LangChain Yahoo Finance tool to DSPy
yahoo_finance_tool = YahooFinanceNewsTool()
finance_news_tool = Tool.from_langchain(yahoo_finance_tool)

class FinancialAnalysisAgent(dspy.Module):
    """Financial analysis agent using ReAct logic."""

    def __init__(self):
        super().__init__()
        self.tools = [
            finance_news_tool,
            get_stock_price,
            compare_stocks
        ]
        self.react = dspy.ReAct(
            signature=FINANCIAL_ANALYSIS_SIGNATURE,
            tools=self.tools,
            max_iters=6
        )

    def forward(self, financial_query: str):
        logger.info(f"Processing query: {financial_query}")
        try:
            result = self.react(financial_query=financial_query)
            logger.info("Agent successfully generated analysis.")
            return result
        except Exception as e:
            logger.error(f"Agent failed to process query: {str(e)}")
            raise e

# Initialize the agent
agent = FinancialAnalysisAgent()

def run_agent(query: str) -> str:
    """Helper function to execute the agent."""
    response = agent(financial_query=query)
    return response.analysis_response
