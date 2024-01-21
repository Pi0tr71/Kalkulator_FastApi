from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import webbrowser


class FuncResult(BaseModel):
    result: float

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/oblicz/{value1}+{value2}', response_model=FuncResult)
def dodawanie(value1: float, value2: float):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid values")

    result = value1 + value2
    return {"result": result}


@app.get('/oblicz/{value1}-{value2}', response_model=FuncResult)
def odejmowanie(value1: float, value2: float):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid values")

    result = value1 - value2
    return {"result": result}

@app.get('/oblicz/{value1}*{value2}', response_model=FuncResult)
def mnozenie(value1: float, value2: float):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid values")

    result = value1 * value2
    return {"result": result}

@app.get('/oblicz/{value1}/{value2}', response_model=FuncResult)
def dzielenie(value1: float, value2: float):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid values")
    if value2 == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Second value can't be 0")
    result = value1 / value2
    return {"result": result}

@app.get('/oblicz/{value1}^{value2}', response_model=FuncResult)
def potegowanie(value1: float, value2: float):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid values")
    result = value1 ** value2
    return {"result": result}

@app.get('/oblicz/{value1}|{value2}', response_model=FuncResult)
def pierwiastkowanie(value1: float, value2: float):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid values")
    if value2 == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Second value can't be 0")
    result = value1 ** (1/value2)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn

    webbrowser.open_new_tab("kalkulator.html")
    uvicorn.run(app, host="127.0.0.1", port=8080)
