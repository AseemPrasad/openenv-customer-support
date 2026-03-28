from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    sender: str  # "customer" or "agent"
    text: str

class CustomerProfile(BaseModel):
    customer_id: str
    satisfaction: float  # 0.0 - 1.0

class ChatState(BaseModel):
    conversation: List[Message]
    customer_profile: CustomerProfile
    pending_queries: int

class Action(BaseModel):
    response: str
    escalate: bool = False