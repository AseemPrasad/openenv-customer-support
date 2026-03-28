from src.chat_env.models import ChatState, Action

def easy_task_grader(state: ChatState, action: Action) -> float:
    """
    Easy task: single FAQ query.
    Grader checks if the agent's response contains the expected keyword.
    """
    expected_answer = "refund"
    if expected_answer in action.response.lower():
        return 1.0
    return 0.0


def medium_task_grader(state: ChatState, action: Action) -> float:
    """
    Medium task: multiple sequential queries.
    Grader computes average satisfaction across queries.
    """
    # Example: satisfaction is tracked in state.customer_profile.satisfaction
    return state.customer_profile.satisfaction


def hard_task_grader(state: ChatState, action: Action) -> float:
    """
    Hard task: multiple simultaneous customers.
    Grader combines satisfaction and resolution rate.
    """
    resolved_fraction = 1.0 - (state.pending_queries / max(1, state.pending_queries + 1))
    score = 0.7 * state.customer_profile.satisfaction + 0.3 * resolved_fraction
    return min(1.0, max(0.0, score))