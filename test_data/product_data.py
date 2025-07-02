from dataclasses import dataclass

@dataclass
class ProductData:
    product_id: int
    product_name: str
    price : int
    #image
    #category

@dataclass
class ProductSearchData:
    search_term: str
    expected_results: bool

product_data_list = [
    ProductData(product_id=2, product_name='Men Tshirt', price=400)
]

product_search_data_list = [
    ProductSearchData(
        search_term="Men Tshirt",
        expected_results=True,
    ),
    ProductSearchData(
        search_term="NonexistentProduct123",
        expected_results=False,
    )
]