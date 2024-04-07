from typing import Union
from app.endpoints.verify import verify
from app.endpoints.currentgradeinfo import current_grade_info
from app.endpoints.pastgpainfo import past_gpa_info
from app.endpoints.studentinfo import student_info

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Zexsys API Version": "0.0.1-async"}


@app.get("/verify")
def read_item(school: str, username: str, password: str):
    return {"authentic": verify(school, username, password)}


@app.get("/currentgradeinfo")
async def read_item(school: str, username: str, password: str):
    shit = await current_grade_info(school, username, password)
    return shit


@app.get("/pastgpainfo")
def read_item(school: str, username: str, password: str):
    return past_gpa_info(school, username, password)


@app.get("/studentinfo")
def read_item(school: str, username: str, password: str):
    return student_info(school, username, password)
