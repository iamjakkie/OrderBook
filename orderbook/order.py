

class Order():
    def __init__(self, side, quantity, price=0):
        self.side = side
        self.quantity = quantity 
        self.price = price 
        self.timestamp = int(time())
        if(price > 0):
            self.type = 'Limit'
        else:
            self.type = 'Market'
            if(side == Side.BUY):
                self.price = sys.maxsize
        self.closed = False

    @property
    def side(self):
        return self._side 

    @side.setter 
    def side(self, side):
        if (isinstance(side, Side)):
            self._side = side

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if(timestamp <= 0):
            raise ValueError("Error, timestamp below 0")
        self._timestamp = timestamp

    @property 
    def quantity(self):
        return self._quantity

    @quantity.setter 
    def quantity(self, quantity):
        if(quantity < 0):
            raise ValueError("Error, quantity below 0")
        elif(quantity == 0):
            self.closed = True
        self._quantity = quantity

    @property 
    def price(self):
        return self._price
    
    @price.setter 
    def price(self, price):
        if(price < 0):
            raise ValueError("Error, price below 0")

        if(price == 0 and self.side == Side.BUY):
            self._price = sys.maxsize
        else:
            self._price = price

    @property 
    def closed(self):
        return self._closed 
    
    @closed.setter 
    def closed(self, closed):
        self._closed = closed
    
    def __lt__(self, other):
        # by date
        return self.timestamp < other.timestamp

    def __repr__(self):
        return '{} Order for {} pieces at {} price created at {}[s] ({})'.format(self.side, self.quantity, self.price, self.timestamp, self.type)