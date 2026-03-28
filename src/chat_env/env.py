from typing import Tuple, Dict
from src.chat_env.models import ChatState, Action, Message, CustomerProfile
from src.chat_env.tasks import easy_task_grader, medium_task_grader, hard_task_grader
from src.chat_env.rewards import compute_reward

class ChatEnv:
    def __init__(self, task_level: str = "easy"):
        self.task_level = task_level
        self.state_data: ChatState = None

    def reset(self) -> ChatState:
        if self.task_level == "easy":
            profile = CustomerProfile(customer_id="cust1", satisfaction=0.5)
            self.state_data = ChatState(
                conversation=[Message(sender="customer", text="How do I get a refund?")],
                customer_profile=profile,
                pending_queries=1
            )
        elif self.task_level == "medium":
            profile = CustomerProfile(customer_id="cust2", satisfaction=0.4)
            self.state_data = ChatState(
                conversation=[
                    Message(sender="customer", text="Where is my order?"),
                    Message(sender="customer", text="Can I change my shipping address?")
                ],
                customer_profile=profile,
                pending_queries=2
            )
        else:  # hard
            profile = CustomerProfile(customer_id="cust3", satisfaction=0.3)
            self.state_data = ChatState(
                conversation=[
                    Message(sender="customer", text="I want a refund."),
                    Message(sender="customer", text="My product arrived damaged."),
                    Message(sender="customer", text="Can I speak to a manager?")
                ],
                customer_profile=profile,
                pending_queries=3
            )
        return self.state_data

    def step(self, action: Action) -> Tuple[ChatState, float, bool, Dict]:
        # Update conversation
        self.state_data.conversation.append(Message(sender="agent", text=action.response))

        # Update satisfaction and pending queries if resolution keyword is present
        if "refund" in action.response.lower():
            self.state_data.pending_queries = max(0, self.state_data.pending_queries - 1)
            self.state_data.customer_profile.satisfaction = min(
                1.0, self.state_data.customer_profile.satisfaction + 0.2
            )

        # Compute reward using rewards.py
        reward = compute_reward(
            action_response=action.response,
            escalate=action.escalate,
            satisfaction=self.state_data.customer_profile.satisfaction,
            pending_queries=self.state_data.pending_queries,
        )

        # Grader score
        if self.task_level == "easy":
            grader_score = easy_task_grader(self.state_data, action)
        elif self.task_level == "medium":
            grader_score = medium_task_grader(self.state_data, action)
        else:
            grader_score = hard_task_grader(self.state_data, action)

        done = self.state_data.pending_queries == 0
        info = {"grader_score": grader_score}

        return self.state_data, reward, done, info

    def state(self) -> ChatState:
        return self.state_data