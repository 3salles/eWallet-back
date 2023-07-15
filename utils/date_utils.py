from datetime import datetime

def convert_to_python_time(date):
    if date is None:
        return datetime.today()
    else:
        date_splited = date.split('-')
        date_array = []

        for index in date_splited:
            date_array.append(int(index))
        
        return datetime(date_array[0], date_array[1], date_array[2])