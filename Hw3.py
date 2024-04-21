from datetime import datetime

def get_days_from_today (date):
    try:
        choosen_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.now()
        delta = current_date - choosen_date
        return delta.days
    except ValueError:
        return ("Невірний формат дати.Використовуй 'YYYY-mm-dd'")  


choosen_date = ("2022-02-24")
print (get_days_from_today(choosen_date))

