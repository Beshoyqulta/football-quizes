from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.answering_sheet import *
from src.reading_sheet import *

app = FastAPI(title="Football Link Test")

csv = read_csv()

class DataResponse(BaseModel):
    player_1: str
    player_2: str
    player_3: str
    player_4: str
    player_5: str

class AnsweringRequest(BaseModel):
    user_answer: str

@app.get("/player-data", response_model=DataResponse)
async def get_sheet_data():
    """
    GET API: Converts the current DataFrame into a JSON response 
    matching the SheetDataResponse schema.
    """
    try:
        return DataResponse(
            player_1= csv['player_1'].iloc[0],
            player_2= csv['player_2'].iloc[0],
            player_3= csv['player_3'].iloc[0],
            player_4= csv['player_4'].iloc[0],
            player_5= csv['player_5'].iloc[0]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")
    

@app.post("/player-guess")
async def guess_the_player(payload: AnsweringRequest):
    check_the_answer = is_the_answeer_correct(payload.user_answer, csv)
    if check_the_answer:
        return "true"
    else:
        return "wrong_answer"
    
