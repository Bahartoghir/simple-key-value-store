from fastapi import FastAPI, HTTPException

app = FastAPI()

store = {}

@app.post("/set")
def set_value(key: str, value: str):
    store[key] = value
    return {"message": "value stored successfully"}

@app.get("/get")
def get_value(key: str):
    if key not in store:
        raise HTTPException(status_code=404, detail="key not found")
    return {"key": key, "value": store[key]}

# this is comment