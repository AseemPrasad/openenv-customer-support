import pytest
from src.chat_env.env import ChatEnv
from src.chat_env.models import Action

def test_reset():
    env = ChatEnv()
    state = env.reset()
    assert state.customer_profile.customer_id == "cust1"

def test_step():
    env = ChatEnv()
    env.reset()
    action = Action(response="Hello!", escalate=False)
    state, reward, done, info = env.step(action)
    assert isinstance(reward, float)
    assert "debug" in info