class Location():
    __slots__ = (
        "longitude",
        "latitude"
    )
    def __init__(self, longitude : int, latitude : int):
        self.longitude = longitude
        self.latitude = latitude
        
    @property
    def link(self):
        return f"https://maps.google.com/maps?q=loc:{self.longitude},{self.latitude}"
    
    @classmethod
    def from_dict(cls, data):
        return cls(longitude = data["longitude"], latitude = data["latitude"])
    
    def to_dict(self):
        data = {}
        
        data["longitude"] = self.longitude if self.longitude is not None else None
        data["latitude"] = self.latitude if self.latitude is not None else None
        
        return data
        