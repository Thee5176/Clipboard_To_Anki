import pyperclip
import pykakasi
import time
from openpyxl import load_workbook


def append_to_spreadsheet(filename, data):
    try:
        workbook = load_workbook(filename)
        sheet = workbook.active
    except FileNotFoundError:
        from openpyxl import Workbook

        workbook = Workbook()
        sheet = workbook.active

    sheet.append(data)
    workbook.save(filename)

def append_clipboard(filename):
    last_text = ""
    print("Clipboard monitor started. Press Ctrl+C to stop.")

    try:
        while True:
            current_text = pyperclip.paste()
            if current_text != last_text and current_text.strip():
                last_text = current_text
                print(f"detect new clipboard item {current_text}.")
                # save copied text into spreadsheet
                append_to_spreadsheet(filename, [current_text])
                print(f"successfully add to spreadsheet")
                
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nClipboard monitor stopped.")

if __name__ == "__main__":
    file = str(input("Choose your file name: ")) + ".xlsx"
    append_clipboard(file)
