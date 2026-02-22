from fastapi import APIRouter, HTTPException
from app.schemas.agent import AgentRequest, AgentResponse
from app.core.langgraph.graph import run_agent
from app.utils.logger import logger

router = APIRouter()

@router.post("/analyze", response_model=AgentResponse)
async def analyze_financials(request: AgentRequest):
    """
    Endpoint to process financial queries using the AI agent.
    """
    try:
        logger.info(f"Received API request: {request.query}")
        analysis = run_agent(request.query)
        return AgentResponse(
            query=request.query,
            analysis=analysis,
            status="success"
        )
    except Exception as e:
        logger.error(f"API Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
