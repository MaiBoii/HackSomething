import uvicorn
from typing import Optional
from fastapi import FastAPI

app=FastAPI()
animals={"cat":"애옹", "dog":"왕","duck":"꽤꽥"}

@app.get("/")
async def home():
    return {"Hello":"World"}

@app.get("/animals/{animal}")
async def animal_cry(animal: str, cry: Optional[int]):

    """
    동물 울음 소리를 cry 횟수만큼 입력
    """

    sound=""
    for time in range(cry):
        sound=sound+animals[animal]+" "
    return {"animal":animal, "sound":sound.strip()}

if __name__ == "__main__":
    uvicorn.run("animal:app", host="0.0.0.0", port=8092, reload=True)