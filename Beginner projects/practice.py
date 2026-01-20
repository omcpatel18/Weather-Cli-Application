# # class TagCloud:

# #     def __init__(self):
# #         self.tags = {}

# #     def add(self,tag):
# #         self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1

# #     def __getitem__(self,tag):
# #         return self.tags.get(tag.lower,0)
    
# #     def __setitem__(self,tag,count):
# #         self.tags[tag.lower()] = count

# #     def __len__(self):
# #         return len(self.tags)
    
# #     def __iter__(self):
# #         return iter(self.tags)
    
# # cloud = TagCloud()
# # cloud["python"] = 10
# # len(cloud)
# # cloud.add("python")
# # cloud.add("python")
# # cloud.add("python")
# # cloud.add("python")
# # cloud.add("python")
# # cloud.add("python")
# # cloud.add("python")
# # cloud.add("sviper")
# # cloud.add("mr.bean")
# # cloud.add("levi")
# # print("Here are items in the Dictonary.")
# # print(cloud.tags)


# # def add(a,b):
# #     print(f"a+b={a+b}")

# # add(80,-60.356)
    

# # def greet(firstname,lastname):
# #     print(f"jay shree krishna., {firstname} {lastname}")
# #     print("avo ne padharo.")

# # greet( "" , "S")

# # def greet(name):
# #     print(f"hi {name}")
# #     print("Hello how are you.")

# # def greet1(name):
# #     return  f"hi {name}"  

# # greet("om")
# # greet1("yashvi")

# # def add(*numbers):
# #     return f"total={sum(numbers)}"

# # print(add(12,5,654,13,78,-1000,655))

# # def save_user(**user):
# #     print(user)

# # save_user(id = 1,name = "John", age = 15)

# # for i in range(6):
# #     print(i)

# # for i in range(5):
# #     if i == 10:
# #         break
# # else:
# #     print("Loop finished normally")

# # string = "Om patel"
# # print(id(string))
# # string1 = string + "Ai/ml Devloper"
# # string = string1
# # print(id(string))

# # print(str.isascii("2025"))

# # string = "Hello its december and its currently to much cold here"
# # # vl1 = string.find("Hello")
# # # vl2 = string[15:25]
# # # print(f"find = {string.find("om")} , value2 = {string.index("Om")}")

# # try:
# #     print(string.index("om"))
# # except ValueError as e:
# #     print(f"Error caught:{e}")

# # a = int(float("10.0"))
# # print(a)

# # if (True):
# #     print("running if condition without else part")

# # i = 0
# # while 1 < 5 :
# #     print( "this is a infinite loop and you cant stop me dumbo. ")

# # list = [15,25,84,1,56,151]

# # print(list[::-1])
# # list.sort(reverse = 'True')
# # print(list)
# # list.sort()
# # print(list)
# # print(list)
# # list.append(155)
# # list.pop(3)
# # list.insert(1,105)
# # print(list)

# # numbers = [
# #     ("product1",15),
# #     ("product2",5),
# #     ("product3",20),
# # ]

# # # def sort_item(item):
# # #     return item[1]

# # numbers.sort(key = lambda item:item[1])
# # print(numbers)

# # prices = [item[1] for item in numbers]
# # print(prices)

# # price1 = list(map(lambda item:item[1],numbers))
# # print(price1)

# # price2 = list(filter(lambda item : item[1]>=6,numbers))
# # print(price2)

# # list1 = [1,2,3]
# # list2 = [4,5,6]
# # print(list(zip(list1,list2)))

# # browsing_session = []
# # browsing_session.append(1)
# # browsing_session.append(2)
# # browsing_session.append(3)
# # browsing_session.append(4)
# # browsing_session.append(5)
# # browsing_session.append(6)
# # print(browsing_session)
# # last = browsing_session.pop()
# # print(last)
# # print(browsing_session)
# # print("redirect",browsing_session[-1])

# # point = 1,2
# # point1 = (1,2) +(3,4) + (5,6)
# # point2 = (6,7)*3
# # print(type(point))
# # print(point)
# # print(point1)
# # print(point2)


# # x = 100
# # y = 200
# # x,y = y,x

# # print(x)
# # print(y)

# # from array import array
# # numbers = array(["i",[1,2,3]])
# # print(numbers)

# # numbers = [1,1,2,34,5,5,6,3,545,3,54,3,4366867,9,867,3534,6]

# # unique = set(numbers)
# # second = {1,4}
# # second.add(45)
# # second.remove(4)
# # len(second)
# # print(unique)
# # print(second)
# # first = unique

# # print( first | second)
# # print( first & second)
# # print( first - second)
# # print( first ^ second)

# # dict = {"x":1,"y":2,"z":3}

# # if "1" in dict:
# #     print(dict["x"])
# # print(dict.get("a"))
# # from sys import getsizeof

# # values1 = (x*2 for x in range(500000))
# # print("gen:",getsizeof(values1))

# # values2 = [x*2 for x in range(500000)]
# # print("list:",getsizeof(values2))

# # # for x in values1:
# # #     print(x)

# # numbers = [1,2,3,4,5,6,7,8,9,10]

# # print(numbers)
# # print(1,2,3)

# # values = list (range(5))
# # values = [*(x*3 for x in range(5)),*"Hello world"]
# # print(values)

# # sentence = "This is a common interview Question."

# # char_frequency = {}
# # for char in sentence:
# #     if char in char_frequency:
# #         char_frequency [char] += 1
# #     else:
# #         char_frequency[char] = 1
# # print(char_frequency)

# # try :
# #     age = int(input("Age"))
# # except ValueError as e:
# #     print("you didn't enter a valid age.")
# # else:
# #     print("No exception were thrown.")

# import requests

# url = "https://api.freeapi.app/api/v1/public/randomjokes"

# querystring = {"limit":"10","query":"science","inc":"categories%2Cid%2Ccontent","page":"1"}

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers, params=querystring)

# # print(response.json())

# def fetch_random_user_freeapi():
#     data = response.json()
# #
#     user_data = data["data"]

#     jokes= user_data["data"]["data"]["0"]["content"]
    
# print(jokes)

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print("data retrieved!")
        data = response.json()
        return data
    else:
        print(f"failed to retrieve infomation {response.status_code}")

pokemon_name = "mewtwo"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Pokemon_name:  {pokemon_info["name"]}")
    print(f"Pokemon_id:  {pokemon_info["id"]}")
    print(f"Pokemon's_weight  {pokemon_info["weight"]}")
    # print(f"{pokemon_info["color"]}")
    print(f"Pokemon's_height  {pokemon_info["height"]}")
    print(f"Pokemon's_type: {pokemon_info["types"][0]["type"]["name"]}")