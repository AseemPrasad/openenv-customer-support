import os
import openai
from src.chat_env.env import ChatEnv
from src.chat_env.models import Action

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_task(task_level: str):
    env = ChatEnv(task_level=task_level)
    state = env.reset()
    done = False
    total_reward = 0.0

    while not done:
        # Send customer message(s) to model
        customer_texts = " ".join([msg.text for msg in state.conversation if msg.sender == "customer"])
        prompt = f"Customer says: {customer_texts}\nRespond as a helpful support agent."

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # lightweight model for baseline
            messages=[{"role": "system", "content": "You are a customer support assistant."},
                      {"role": "user", "content": prompt}]
        )

        agent_reply = response["choices"][0]["message"]["content"]

        # Create action
        action = Action(response=agent_reply, escalate=False)

        # Step environment
        state, reward, done, info = env.step(action)
        total_reward += reward

    print(f"Task: {task_level}, Total Reward: {total_reward:.2f}, Grader Score: {info['grader_score']:.2f}")

if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)