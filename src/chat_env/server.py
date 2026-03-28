from fastapi import FastAPI
from openenv_core.server import OpenEnvServer
from src.chat_env.env import ChatEnv

def main():
    env = ChatEnv()
    server = OpenEnvServer(env)
    app = FastAPI()
    server.register_routes(app)
    return app

# For uvicorn
app = main()