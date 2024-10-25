from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import json
from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fastapi import FastAPI
import db
from db import cursor
from db import conn


app = FastAPI()


@app.get("/api/gps")
async def get_kullanici(
    unit: str = None, speed: int = None, location: str = None, recordTime: str = None, googleLink: str = None
):
    drop()
    today = datetime.today().date()
    
    cursor.execute('''
    INSERT INTO records (unit,speed, location, recordTime, googleLink, date, read)
    VALUES( ?,	?, ?, ?, ?, ?, 0);
    ''', (unit, speed, location, recordTime, googleLink, today))
    conn.commit()

    return {"unit": unit, "speed": speed, "location": location, "recordTime": recordTime, "googleLink": googleLink}

@app.get("/api")
async def get_records():
    drop()
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    
    rows = db.execute('''
    SELECT * from records
    ''').fetchall()
    
    return json.dumps([dict(ix) for ix in rows])

def drop():
    today = datetime.today().date()
    #yesterday = today - timedelta(days=1)
    ab = conn.cursor()
    ab.execute('''
    DELETE from records WHERE date IS NOT ?
    ''',(today,))
    conn.commit()
    print(today)
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
