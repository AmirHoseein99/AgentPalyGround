from fastapi import APIRouter, HTTPException
from .agent import call_agent
from ..logger import get_logger

agent_router = APIRouter(
    prefix="/agent",
    tags=["agent"]
)

@agent_router.post("/call_agent")
async def call_agent_endpoint(user_input: str):
    logger = get_logger('agent_api')
    logger.info(f"Received user input: {user_input}")
    try:
        response = call_agent(user_input)
        logger.info(f"Agent response: {response}")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error calling agent: {e}")
        raise HTTPException(status_code=500, detail=str(e))