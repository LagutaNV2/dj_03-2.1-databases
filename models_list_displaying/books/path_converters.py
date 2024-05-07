from datetime import datetime


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'
    
    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format)
    
    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)
    
    # def to_python(self, value):
    #     # Convert the matched value to a Python `datetime.date` object
    #     return datetime.strptime(value, '%Y-%m-%d').date()
    #
    # def to_url(self, value):
    #     # Convert the Python `datetime.date` object to a string representation suitable for URLs
    #     return value.strftime('%Y-%m-%d')