age=12
print(id(age))
age=23
print(id(age))
age=12
print(id(age))

spice_mix=set()
print(f"Initial spice mix Id:{id(spice_mix)}")
spice_mix.add('Ginger')
spice_mix.add('cardamom')
print(f"Second spice mix Id:{id(spice_mix)}")

is_boiling=True
num_count=5
res=is_boiling+num_count  # upcasting
print(f"val : {res}")

#logical operator
water_hot=True
tea_added=False
can_serve=water_hot or tea_added
print(f"can serve chai : {can_serve}")

shop_closed=False
can_entered=not shop_closed
print(can_entered)

# String in python

s="this is the python code"
print(s[:1])
print(s[0:10:3])
print(s[::-1])

#Tuple
masala_spices=('Cardamom','cloves','Cinnamon')
# print(masala_spices[0])
(spice1,spice2,spice3)=masala_spices
print(f"Main masala spices{spice1,spice2,spice3}")

Ginger_ratio,Cardamom_ratio=2,1
print(f"{Ginger_ratio},{Cardamom_ratio}")
Ginger_ratio,Cardamom_ratio=Cardamom_ratio,Ginger_ratio
print(f"{Ginger_ratio},{Cardamom_ratio}")

#List means we can mute the list
ingredients=["milk","Water","black tea"]
ingredients.append("sugar")
ingredients.insert(1,"coffee")
ingredients.pop()
ingredients.pop(1)
res=ingredients.count
print(res)
print(f"{ingredients}")

spice_option=["ginger","cardamom"]
chai_ingredients=["black-tea","milk","powder","boil_water"]
chai_ingredients.extend(spice_option)
print(f"{chai_ingredients}")
chai_ingredients.insert(1,"nandini_milk")
print(chai_ingredients)
# chai_ingredients.clear()
print(chai_ingredients.index("nandini_milk"))
chai_ingredients.reverse()
chai_ingredients.sort()
print(chai_ingredients)
print(chai_ingredients)
print(chai_ingredients)

#operator overloading 
base_liquid=["Water","milk"]
extra_flavor=["ginger"]
full_liquid_mix=base_liquid+extra_flavor
print(full_liquid_mix)

base_liquid=["Water","milk"] * 3
print(base_liquid)

sugar_level=[1,2,3]
print(max(sugar_level))
print(min(sugar_level))
name_list=bytearray(b"sachin")
res=name_list.replace(b"sac",b"abc")
print(res)

chai_order=dict(type="Masala_chai", size='large', sugar=2)
print(chai_order)
print(chai_order.keys())
print(chai_order.values())
chai_order["base"]="milk"
print(chai_order)
del chai_order["base"]
print(chai_order)
chai_order.update({"ginger":True,"price":90})
print(chai_order)

print({"ginger" in chai_order})
print("ginger" in chai_order)
print(chai_order.items())

res=chai_order.popitem()
print(res)
print(chai_order)

kettle_boiled=True
if kettle_boiled:
    print("done")

input_size=input("Enter the size of the tea small/medium/large}").lower()
if input_size == "small":
    print("rupees 10")
elif input_size == 'medium':
    print('20rs')
elif input_size == 'large':
    print('30rs')
else:
    print("invalid input")
    

device_status = "active"
Temperature = 37

if device_status == "active":
    if Temperature >35:
        print("High Temperature alert!")
    else:
        print("Temp is normal")
else:
    print("Device is offline")


delivery_fees=int(input("Enter the amount for the delivery"))
delivery_fees = 0 if delivery_fees>300 else 30
print(delivery_fees)


seat_type = input("Enter the seat type AC/Sleeper/3A/2A")

match seat_type:
    case "AC":
        print("AC")
    case "Sleeper":
        print("Sleeper")
    case "3A":
        print("3A")
    case "2A":
        print("2A")
    case _:
        print("invalid")
        
        















