import sqlite3

from app_paths import DB_PATH


def get_meter_data(name):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute('SELECT date, value FROM meter WHERE name=?', (name,))
    for date, value in cur:
        yield {'date': date, 'value': value}

    con.close()


def entries_exist(table, name):
    if table != 'meter':
        return False

    data_for_name = list(get_meter_data(name))
    return len(data_for_name) > 0