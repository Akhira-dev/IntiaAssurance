import random,string
from insurance_management.models import Insurance



def generate_insurance_code():
        while True:
            random_number = ''.join(random.choices(string.digits,k=5))
            insurance_code = f'IA{random_number}'
            if not Insurance.objects.filter(insurance_code=random_number).exists():
                return insurance_code