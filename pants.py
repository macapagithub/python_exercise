class Pants:
    
    def __init__(self, pant_color: str, waist_size: int, length: int, pant_price: float):
        """
        Method for initializing a Pants object
    
        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)
            
        Attributes:
            color (str): color of a pants object
            waist_size (int): waist size of a pants object
            length (int): length of a pants object
            price (float): price of a pants object
        """

        self.color = pant_color
        self.waist_size = waist_size
        self.length = length
        self.price = pant_price

    
    def change_price(self, new_price: float) -> float:
        self.price = new_price

    def discount(self, discount: float) -> float:
        return self.price * (1-discount)
