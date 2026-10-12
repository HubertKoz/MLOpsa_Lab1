from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "asdf"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
