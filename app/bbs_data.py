import os, json, datetime

BASE_DIR = os.path.dirname(__file__)
SAVE_FILE = BASE_DIR + '/data/log.json'

def load_data():
    if not os.path.exists(SAVE_FILE):
        return []
    with open(SAVE_FILE, 'rt', encoding='utf-8') as f:
        return json.load(f)

def save_data(data_list):
    with open(SAVE_FILE, 'wt', encoding='utf-8') as f:
        json.dump(data_list, f)

def save_data_append(user, text):
    tm = get_datetime_now()
    data = {'name':user, 'text':text, 'date':tm}
    data_list = load_data()
    data_list.insert(0, data)
    save_data(data_list)

def get_datetime_now():
    now = datetime.datetime.now()
    return "{0:%Y/%m/%d %H:%M}".format(now)