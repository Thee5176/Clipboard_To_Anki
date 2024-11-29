import pyperclip
import pykakasi
import time
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


"""
/ Step 1: parse clipboard > py_list
/ Step 2: loop until KeyboardInterupt
TODO Step 3: select sheet_name
Step 4: iterate through py_list
    / 4.1; parse py_list's item > column A
    / 4.2; find furigana > column B
    / 4.3; tag > column C FIXME APPEND ONLY ONE LINE??
"""

#Step 4
def append_to_spreadsheet(filename, column_no, dataset):
    try:
        workbook = load_workbook(filename)
        sheet = workbook.active
    except FileNotFoundError:
        from openpyxl import Workbook

        workbook = Workbook()
        sheet = workbook.active
    
        #Step 4.2
    if type(dataset) == str:
        #find last row of prev column
        prev_column = get_column_letter(column_no - 1)
        row_with_data = [cell for cell in sheet[prev_column] if cell.value is not None]
        last_row = int(row_with_data[-1].row) + 1  if row_with_data else 1
        
        #append text into all collumn
        column = get_column_letter(column_no)
        for i in range(1, last_row):
            sheet[f"{column}{i}"] = dataset
              
    #Step 4.1, 4.3
    else:
        #find last row of that column
        column = get_column_letter(column_no)
        row_with_data = [cell for cell in sheet[column] if cell.value is not None]
        next_row = int(row_with_data[-1].row) + 1  if row_with_data else 1
        
        #append data from list
        for data in dataset:
            sheet[f"{column}{next_row}"] = data
            next_row = next_row + 1



    workbook.save(filename)

def find_furigana(dataset):
    kks = pykakasi.kakasi()
    furigana_list = []
    
    for data in dataset:
        result = kks.convert(data)       #result in dictionary of generator object
        furigana = "".join(item['hira'] for item in result) #convert generator obj > str
        furigana_list.append(furigana)
        
    return furigana_list


def append_clipboard(filename):
    saved_words = []
    last_text = ""
    print("Clipboard monitor started. Press Ctrl+C to stop.")

    first_clip = True
    
    try:
        while True:
            current_text = pyperclip.paste()
            if current_text != last_text and current_text.strip():
                last_text = current_text
                
                if first_clip:
                    #skip first clipboard value
                    first_clip = False
                    print(f"ignored first clipboard item: {current_text}")
                    continue

                print(f"Detect new clipboard item: {current_text}.")
                
                # append new word to list
                saved_words.append(current_text)
                print(f"Saved new item: {current_text}.")            
                
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nClipboard monitor stopped.")
        
        append_to_spreadsheet(filename, 1, saved_words)
        print("Parsed clipboard to spreadsheet")
        
        furigana_list = find_furigana(saved_words) #TODO read words from column
        append_to_spreadsheet(filename, 2, furigana_list)
        print("Appended furigana")
        
        tag = input('Add a tag: ') #TODO add more than 1 tag
        append_to_spreadsheet(filename, 3, tag)
        print("Appended tag")
        
if __name__ == "__main__":
    file = "Anki.xlsx"
    append_clipboard(file)
