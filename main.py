# pip install pandas
from csv import excel
import pandas as pd
# pip install numpy
import numpy as np
import PySimpleGUI as sg
import os
from table import create_table

working_directory = os.getcwd()

layout = [  
            [sg.Text("Choose a CSV file:")],
            [sg.InputText(key="-FILE_PATH-"), 
            sg.FileBrowse(initial_folder=working_directory, file_types=[("Excel Files", "*.xlsx")])],
            [sg.Button('Submit'), sg.Exit()]
        ]

window = sg.Window("Display CSV", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Submit":
        excel_file = values["-FILE_PATH-"]
        excel_file_array = pd.read_excel(excel_file)
        # Get the first row (ndarray)
        headers = excel_file_array.columns.to_numpy()
        # Get the actual data (ndarray)
        data_array = excel_file_array.to_numpy()
        # Convert ndarrays to Python lists
        create_table(data_array.tolist(), headers.tolist())
window.close()

