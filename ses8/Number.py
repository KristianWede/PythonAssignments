class Car:
    def __init__(self, make, model, bhp, mph):
        self._make = make
        self._model = model
        self._bhp = bhp
        self._mph = mph

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        self._make = new_make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @property
    def bhp(self):
        return self._bhp

    @bhp.setter
    def bhp(self, new_bhp):
        self._bhp = new_bhp

    @property
    def mph(self):
        return self._mph

    @mph.setter
    def mph(self, new_mph):
        self._mph = new_mph

    def get_car_info(self):
        return f"Make: {self.make}, Model: {self.model}, BHP: {self.bhp}, MPH: {self.mph}"

car1 = Car("Toyota", "toyotabutmodel", "toyotabutbhp", 124)
print(car1.get_car_info())
print(car1.bhp)
