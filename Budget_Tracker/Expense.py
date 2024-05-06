class Expense:

    def __init__(self, name, category, amount) -> None:
        self.name= name
        self.category= category
        self.amount= amount 
    
    def __repr__(self) -> str:
        return "<Expense:{0}, {1}, {2}>".format(self.name, self.category, self.amount)