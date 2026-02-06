def pour_chai(n):
    print(n)
    if n==0:
        return "chai is not available"
    return pour_chai(n-1)
res=pour_chai(3)
print(res)

list_values=["ginger","light","kadak","ginger"]
chai_values=list(filter(lambda chai:chai!="ginger",list_values))
print(chai_values)

#list Comprehensions
menu=[
    "ginger tea",
    "lemon tea",
    "green tea",
    "Iced peach tea",
    "Iced lemon peach tea",
]

iced_tea=[tea for tea in menu if "Iced" in tea]
print(iced_tea)

len_tea=[tea for tea in menu if len(tea)>2]
print(len_tea)

number=[1,2,3,4,5]
square=[]
for n in number:
    square.append(n*n)
print(square)   

square=[n*n for n in number]
print(square)

num=[1,2,3,4,5,6]
even_num=[n for n in num if n%2==0]
print(even_num)

num=[1,2,3,4,5]
res=["even" if n%2==0 else "odd" for n in num]
print(res)

fav_chai=["masala chai", "green chai", "lemon chai", "elachi chai", "green chai", "masala chai" ]
res=[chai for chai in fav_chai]
result={chai for chai in fav_chai if len(chai)>10}
print(res)
print(result)

recipes={
    "masala chai":["ginger","black paper","milk"],
    "elachi chai":["cardamom","milk"],
    "spicy chai":["ginger","black paper","milk"],
}
print()
res={spices for chai in recipes.values() for spices in chai }
print(res)

# dict comprehensions
chai_prices={
    "masala_chai":40,
    "green_chai":90,
    "lemon_chai":50,
}
res={tea:price/80 for tea, price in chai_prices.items()}
print(res)



