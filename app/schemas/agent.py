from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    query: str = Field(..., description="The financial query to analyze", example="What is the stock price of Apple?")

class AgentResponse(BaseModel):
    query: str
    analysis: str
    status: str = "success"
