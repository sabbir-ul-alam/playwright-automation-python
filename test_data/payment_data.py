from dataclasses import  dataclass

@dataclass
class PaymentData:
    name_on_card: str
    card_number: str
    cvc: str
    expire_month : str
    expire_year: str


payment_data_list = [
    PaymentData(
        name_on_card='sabbir',
        card_number='1234567890',
        cvc='124',
        expire_month='4',
        expire_year='2037'
    )
]