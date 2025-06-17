from dataclasses import dataclass

@dataclass
class LoginData:
    email: str
    password: str
    valid: bool
    user_name:str


login_data_list = [
    LoginData(email='sualsabbir@gmail.com', password='123456789', valid=True, user_name='Sabbir'),
    LoginData(email='sualsabbir@gmail.com', password='1', valid=False, user_name = 'Sabbir'),

]