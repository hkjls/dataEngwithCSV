import pandas as pd
import xlwings as xl

def df_from_excel(file, sheet_name):
    app = xl.App(visible=False)
    book = app.books.open(file)
    book.save()
    app.kill()
    return pd.read_excel(file, sheet_name=sheet_name)