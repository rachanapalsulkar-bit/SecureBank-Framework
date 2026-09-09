from datetime import datetime


class DataGenerator:
    @staticmethod
    def generate_email():
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        return f"test_{timestamp}@acldigital.com"


def data_generator():
    return DataGenerator.generate_email()
