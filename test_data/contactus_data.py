from dataclasses import dataclass

@dataclass
class ContactUs:
    name: str
    email: str
    subject: str
    message_body: str
    file_path: str


contactus_data_list = [
    ContactUs(
        name='sabbir',
        email='sualsabbir@gmail.com',
        subject='Test file upload',
        message_body='The is the message body',
        file_path="C:/Users/Sabbir/Downloads/01d@2x.png"
    )
]
