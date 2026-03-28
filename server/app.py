from fastapi import FastAPI
from openenv_core.server import OpenEnvServer
from src.chat_env.env import ChatEnv

def main():
    # Initialize environment
    env = ChatEnv()
    server = OpenEnvServer(env)
    app = FastAPI()
    server.register_routes(app)
    return app

# Uvicorn will look for this
app = main()

# Allow direct execution
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=False)