import json
import os 


#זה המסלול הקבוע שלנו לתיקיה עם הנתונים והנתוני מוק שהבאתם לנו 
DATA_FOLDER = os.path.join(os.path.dirname(__file__),"data")


def load_data(file_name):
    file_path = os.path.join(DATA_FOLDER, file_name)
    #במקרה שהנתיב לא יהיה תקין נחזיר רישמה ריקה 
    if not os.path.exists(file_path):
        return[]
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def save_data(file_name, data):
    file_path = os.path.join(DATA_FOLDER, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)#ascii=זה לכתיבה בשפה העברית שיראה תקין