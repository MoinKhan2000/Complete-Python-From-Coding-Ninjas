a = {"Moin Khan", "ABC"}
# print(type(a))  # set
a = {"Moin Khan": "CSE", "Manish": "ABC", 10: 10}
print(type(a), a)  # dict {'Moin Khan': 'CSE', 'Manish': 'ABC', 10: 10}
b = {}
# print(type(b))  # set

# Getting the len(dict)
# print(len(a))  # 3

b = a
# print(b)
print("a ", a)
b[0] = "Mohsin Khan"  # 0: 'Mohsin Khan'
print("b ", b)
print("a", a)  # When b is changing a is also changing  !Problem

# Without using a a.copy function the variable will start to reference same dictionary

a = {"Moin Khan": "CSE", "Manish": "ABC", 10: 10}
print("a", a)  # a {'Moin Khan': 'CSE', 'Manish': 'ABC', 10: 10}
b = a.copy()
b[0] = "hey I am B"  # b {'Moin Khan': 'CSE', 'Manish': 'ABC', 10: 10, 0: 'hey I am B'}
print("b", b)
print("a", a)  # a {'Moin Khan': 'CSE', 'Manish': 'ABC', 10: 10}


# Another way to create a dictionary

# If the same key is present then the reference is updated
c = dict([("Hii", "Harish"), ("Hii", "Moin")])
print(c)  # {'Hii': 'Moin'}
# If the same key is present then the reference is updated
c = dict([("Hii", "Harish"), ("Hello", "Moin")])
print(c)  # {'Hii': 'Harish', 'Hello': 'Moin'}


# Yet Another Way To Create A Dict

# d=dict.fromkeys(["Hii",1,2,])
# print(d) #{'Hii': None, 1: None, 2: None}
d = dict.fromkeys([1, 2, 3, 4])
print(d)
# {1: None, 2: None, 3: None, 4: None}
d = dict.fromkeys([1, 2, 3, 4], [1, 2, 3, 4])
print(d)
# {1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]}
