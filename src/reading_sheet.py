import pandas as pd 

def read_csv():
    sheet_id = "1_7c15EyzuiIO5dfW-lXiSgY4OxvcH3vVBqB0xDbHS48"
    sheet_name = "Sheet1"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    csv = pd.read_csv(url)
    return csv
