from fastapi import FastAPI 
import streamlit as st
from web_app_v3 import main
app = FastAPI()



@app.get("/streamlit")
async def main():
    return main()
