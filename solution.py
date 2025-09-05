solution.py
`python
#!/usr/bin/env python3
# solution.py — Lab-6 (OOP variant 1)

class Building:
    def init(self, area, price_per_m2, residents):
        self.area = area
        self.price_per_m2 = price_per_m2
        self.residents = residents
    def total_cost(self):
        return self.area * self.price_per_m2
    def cost_per_resident(self):
        return self.total_cost() / self.residents if self.residents else float('inf')

class VillageHouse(Building):
    def init(self, area, price_per_m2, residents, has_garden=True):
        super().init(area, price_per_m2, residents)
        self.has_garden = has_garden
    def description(self):
        return f"VillageHouse area={self.area}, garden={self.has_garden}"

class ApartmentBuilding(Building):
    def init(self, area, price_per_m2, residents, floors=1):
        super().init(area, price_per_m2, residents)
        self.floors = floors
    def description(self):
        return f"ApartmentBuilding area={self.area}, floors={self.floors}"

if name == 'main':
    b1 = VillageHouse(120, 50000, 4, has_garden=True)
    b2 = ApartmentBuilding(2000, 70000, 40, floors=10)
    for b in (b1,b2):
        print(b.description())
        print("Total cost:", b.total_cost())
        print("Cost per resident:", b.cost_per_resident())
        print()
