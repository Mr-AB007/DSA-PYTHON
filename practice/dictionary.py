person = {"name": "Bittu", "city1": "Patna", "age1": 25, 123 : "number"} #key can be for any primitive data type int,string,bool

# this dict() constructor key should always be string and valid variable name
student = dict(name = "Anubhav", city =  "Pune", age = 24) 

def main1():
    # print(person)
    # print(student)

# Accessing in dictionary

    # print(f"Person : {person["age"]}") 
    # print(f"Student : {student.get("age")}")

    # print(f"{student.get("123")}") #output->   None
    # print(f"{person["pin"]}") #output-> it will give error you cant search for non-existing key

# you can modify value of key but u cant modify key

    # student["age"] = 35 
    # print(f"New Age: {student['age']}")

#deletion in dictionary 
    # person.pop("age")  # Removes 'age' key
    # del person["city"]  # Deletes 'city' key
    # person.clear()  # Removes all elements
    # print(person)  # {}

# Iteration of Dictionary
    
    # for key in student.keys():
    #     print(key)  # name, age, city

    # for value in student.values():
    #     print(value)  # Anubhav, 25, Patna

    # for key, value in student.items():
    #     print(f"{key}: {value}")  # name: Anubhav, age: 25, city: Patna

# Special Dictionary Tricks

    # square = {x: x*x for x in range(1,6)} #this statement means: create dictinare for key = x(1,2,3,4,5) and value = sqaure of 1,2,3,4,5
    # print(square) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

# Add only if the key does not already exist in the dictionary. If the key exists, it does not change its value.
    # person.setdefault("salary", 50000)  # Adds 'salary' if not present
    # print(person["salary"])  # 50000

# Merging two dictionary 
    # merged = {1:1,2:4} | {3:9,4:16} # you can also do person | student but keys should unique in both
    # print(merged)  #{1: 1, 2: 4, 3: 9, 4: 16}



# defaultdict() automatically provides a default value for missing keys instead of raising a KeyError
    from collections import defaultdict

    # dd = defaultdict(int)
    # dd["a"] += 1
    # print(dd)  # defaultdict(<class 'int'>, {'a': 1}) even there was value for a before it return 0 + 1 = 1

    # dd = defaultdict(int)  # Default value is `int()`, which is 0
    # print(dd["a"])  # ✅ No KeyError, returns 0

    person = {"name": "Anubhav"}
    person.setdefault("hobbies", []).append("Coding")  # Adds a list and appends "Coding"
    person.setdefault("hobbies", []).append("Gaming")  # Appends "Gaming"

    print(person)

if __name__ == "__main__":
    main1()

"""
✅ Use .get() to avoid KeyError
✅ Use dictionary comprehension for concise code
✅ Use defaultdict for missing keys
✅ Avoid using mutable objects as keys

"""


# Tricky Dictionary Questions 
d = {}
d[1] = "One"
d[True] = "True"
d[1.0] = "Float"

print(d) #1,True,1.0 in python are same so output-> 1 : Float , means keys are same so only value is updated

d = {"a": 1, "b": 2}
d["c"] = d.get("c", 0) + 1

print(d) # d.get("c", 0) returns 0 since "c" does not exist, then +1 is added.

