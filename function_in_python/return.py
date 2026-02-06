def make_chai():
    return "Chai for sachin"
print(make_chai())

def make_chai():
    pass
print(make_chai())

def make_chai():
    return 20
print(make_chai())

def make_chai():
    return 100, 200
print(make_chai())

def sold_cup():
    return 100,250
total_cup=sold_cup()
print(total_cup)

def chai_status(cups_left):
    if cups_left==0:
        return "Sorry don't have chai"
    return "few cups left the chai"
print(chai_status(0))
print(chai_status(5))


    

