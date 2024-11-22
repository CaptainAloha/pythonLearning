# whisky.py

class WhiskyKlasse:
    def __init__(self, name, taste, country):
        self.name = name
        self.taste = taste
        self.country = country

    def GetName(self):
        return self.name
    
    def GetTaste(self):
        return self.taste
    
    def GetCountry(self):
        return self.country