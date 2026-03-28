import pytest
from src.chat_env.rewards import compute_reward

def test_empathy_bonus():
    reward = compute_reward("I'm sorry to hear that", escalate=False, satisfaction=0.5, pending_queries=1)
    assert reward >= 0.1

def test_resolution_bonus():
    reward = compute_reward("We will process your refund", escalate=False, satisfaction=0.5, pending_queries=1)
    assert reward >= 0.2

def test_escalation_penalty():
    reward = compute_reward("Let me escalate this", escalate=True, satisfaction=0.5, pending_queries=1)
    assert reward <= 0.0  # penalty applied

def test_progress_bonus():
    reward = compute_reward("Refund processed", escalate=False, satisfaction=0.5, pending_queries=0)
    assert reward >= 0.3

def test_combined_rewards():
    reward = compute_reward("Sorry, refund processed", escalate=False, satisfaction=0.5, pending_queries=0)
    # empathy + resolution + progress
    assert reward >= 0.6