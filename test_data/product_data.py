
from dataclasses import dataclass

@dataclass
class ProductData:
    product_id : int
    product_name: str
    #image
    #category


product_data_list = [
    ProductData(product_id=2, product_name='Men Tshirt')
]