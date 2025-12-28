from datetime import datetime

class EntryDateTimeRepo:
    def get_current_datetime(self):
        return datetime.now()

    def extract_date(self, dt: datetime):
        return dt.date()