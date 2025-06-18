from dataclasses import dataclass


@dataclass
class UserRegisterData:
    title: str
    name: str
    email: str
    password: str
    day: str
    month: str
    year: str
    first_name: str
    last_name: str
    company: str
    address: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile: str
    existing: bool


user_registration_data_list = [
    UserRegisterData(
        title="Mr.",
        name="Sabbir",
        email="ssualsabbir@gmail.com",
        password="123456789",
        day="29",
        month="10",
        year="1996",
        first_name="Sabbir Ul Alam",
        last_name="Sabbir",
        company="tigerit",
        address="Matikata",
        country="United States",
        state="Chicago",
        city="Illinois",
        zipcode="34430",
        mobile="01558258590",
        existing=False
    ),
    UserRegisterData(
        title="Mr.",
        name="Sabbir",
        email="sualsabbir@gmail.com",
        password="123456789",
        day="29",
        month="10",
        year="1996",
        first_name="Sabbir Ul Alam",
        last_name="Sabbir",
        company="tigerit",
        address="Matikata",
        country="United States",
        state="Chicago",
        city="Illinois",
        zipcode="34430",
        mobile="01558258590",
        existing=True
    ),

]
