from fastapi import FastAPI, HTTPException
from getTemple import getTem
from fastapi.responses import FileResponse
app = FastAPI()


@app.get("/temple/{provide_name}")
def getTemple(provide_name):
    print("eiei")
    li_match = getTem(provide_name)
    return li_match


@app.get("/temple/list_of_temple-csv")
def download_csv():
    # print("eiei")
    # print("eiei")
    # retur"n FileResponse("list_temple.csv", media_type="text/csv", filename="list_temple.csv")
    return "eieiei"
