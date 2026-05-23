# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def root():
#     return {"message": "Hello from sample-mcp!"}


# def main():
#     print("Hello from sample-mcp!")

# only run with uv run main.py
# if __name__ == "__main__":
#     main()

# 2nd way to do it, using startup event

# from fastapi import FastAPI

# app = FastAPI()


# @app.on_event("startup")
# async def startup_event():
#     print("Hello from sample-mcp!")


# @app.get("/")
# def root():
#     return {"message": "Hello from sample-mcp!"}

# 3rd way to do it , using lifespan context manager

from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code (runs when server starts)
    print("Hello from sample-mcp!")

    yield  # app runs here

    # Shutdown code (runs when server stops)
    print("Shutting down sample-mcp!")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Hello from sample-mcp!"}