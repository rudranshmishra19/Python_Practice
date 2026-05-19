class Building:
    def __init__(self,height,rooms,family):
        self.height=height
        self.rooms=rooms
        self.family=family

class owner:
    def __init__(self,owner_name):
        self.name=owner_name

class property(Building,owner):
    def __init__(self, height, rooms,owner_name,location,family):
        Building.__init__(self,height,rooms,family)  #fixed -
        owner.__init__(self,owner_name)
        self.location=location


class family(Building):
    def __init__(self, height, rooms, family,members):
        super().__init__(height, rooms, family)
        self.members=members
# Building has quanity such as height,roomno,family members
class members_name(family):
    def __init__(self, height, rooms, family, members,name):
        super().__init__(height, rooms, family, members)
        self.name=name
# Create object
f=members_name(5,10,400,4,'Deshmukh')
p=property(5,100,400,'Mishra','Mumbai')
print(f.height)
print(f.rooms)
print(f.family)
print(f.members)
print(f.name)

print(p.height)
print(p.rooms)
print(p.name)
print(p.location)
