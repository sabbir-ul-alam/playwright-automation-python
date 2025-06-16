from dataclasses import dataclass

@dataclass
class UserRegisterData:
    title : str = "Mr."
    name: str = "Sabbir"
    email: str = "ssualsabbir@gmail.com"
    password: str = "123456789"
    day: str = "29"
    month: str = "10"
    year: str = "1996"
    first_name: str = "Sabbir Ul Alam"
    last_name: str = "Sabbir"
    company: str = "tigerit"
    address: str = "Matikata"
    country: str = "United States"
    state: str = "Chicago"
    city: str = "Illinois"
    zipcode: str = "34430"
    mobile: str = "01558258590"