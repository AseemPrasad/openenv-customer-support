def compute_reward(action_response: str, escalate: bool, satisfaction: float, pending_queries: int) -> float:
    """
    Reward shaping logic:
    - Empathy bonus if agent says 'sorry'
    - Resolution bonus if agent mentions 'refund'
    - Penalty for unnecessary escalation
    - Bonus if pending queries are resolved
    """

    reward = 0.0

    # Empathy bonus
    if "sorry" in action_response.lower():
        reward += 0.1

    # Resolution bonus
    if "refund" in action_response.lower():
        reward += 0.2

    # Escalation penalty
    if escalate:
        reward -= 0.2

    # Progress bonus: all queries resolved
    if pending_queries == 0:
        reward += 0.3

    # Clamp reward between 0 and 1
    return max(0.0, min(1.0, reward))