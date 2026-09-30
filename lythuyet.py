#kiểu dữ liệu
#1. int
x = 5
print(type(x)) 
#2. float
y = 3.14
print(type(y))
#3. str
name = "Alice"
print(type(name))
name1 = "Nguyen Tat Thang"
print(name1.upper())
print(name1.lower())
print(len(name))
first_name = "Nguyen"
last_name = "Thang"
full_name = first_name + " " + last_name
print(full_name)
#4. bool
is_true = True
print(type(is_true))
#5. list
player = ["pedro", "Mount", "Kante"]
print(type(player))
player.append("Pulisic")
print(player)
player.remove("Mount")
print(player)
#6. tuple
number = (10, 20)
print(type(number))
#7. set
fruits = {"apple", "banana", "orange", "apple", "banana", "orange"}
print(type(fruits))
#8. dict
person = {"name": "Alice", "age": 25, "city": "New York"}
print(type(person))
print(person["name"])
person.get("age")
print(person.get("age"))
person.keys()
print(person.keys())
for key, value in person.items():
    if value == "Alice":
        print(key)
person.values()
print(person.values())
#9. None
value = None
print(type(value))
#list comprehension là gì
numbers = [1, 2, 3, 4, 5]
result = [number * 2 for number in numbers]
print(result)  
#Fuction là gì, hoạt động như nào
def hello():
    print("Hello, world!")
hello()
def chelsea(player):
    print("Chelsea player:", player)
chelsea("Kante")
#*args / **kwargs hoạt động như nào
#*args hoạt động như một tuple, cho phép bạn truyền một số lượng 
# không xác định các đối số vị trí vào một hàm.
#tuple là một kiểu dữ liệu trong Python, nó là một tập hợp các giá trị 
# không thay đổi (immutable) và được đặt trong dấu ngoặc đơn ().
def Chelsea1(*players):
#1
    print(players)
Chelsea1("Kante", "Mount", "Pulisic")
#2
 #   for player in players:
  #      print(player)
#**kwargs hoạt động như một dictionary, cho phép bạn truyền một số lượng 
# không xác định các đối số từ khóa vào một hàm.
def Chelsea2(**players):
#1

    for key, value in players.items():
        print(key, ":", value)
#2
       #   print(players)
       # Chelsea2(name="Cole", age=23, Nationality="England")
def create_ticket(title, status="Mới"):
    print(title, status)
def hello(name):
    print(f"Xin chào {name}")
def hello1():
    print("Xin chào")
create_ticket("Lỗi đăng nhập")
hello("Thang")
hello1()
#Hàm init hoạt động như nào
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Player {self.name} is {self.age} years old.")

player = Player("Thang", 11)
player1 = Player("Huy", 11)
player2 = Player("Duc", 11)

class ChelseaPlayer(Player):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
        print(f"{self.name} plays as a {self.position}.")   

class Player:
    def introduce(self):
        print("Tôi là cầu thủ")
introduce_player = Player()
introduce_player.introduce()
print(introduce_player)
print(id(introduce_player))
# Class sẽ tạo ra object, sau đó gán object đó vào biến introduce_player. Khi gọi hàm introduce(), nó sẽ lấy thông tin từ object đã tạo từ trước đó và gán dữ liệu vào hàm introduce(). 
# Vì vậy, khi gọi introduce_player.introduce(), nó sẽ in ra "Tôi là cầu thủ" từ object introduce_player.
#Class  = khuôn
#Object = thứ được tạo từ khuôn
#Variable = tên tham chiếu tới object
#Method = hành động của object
# Self 
# Là tham chiếu tới object hiện tại, nó được sử dụng để truy cập các 
# thuộc tính và phương thức của object đó. 
# Khi bạn gọi một phương thức của một object, Python sẽ tự động truyền object đó 
# làm đối số đầu tiên cho phương thức, và self sẽ trỏ tới object đó.
class Player:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Tôi là cầu thủ {self.name}")


class Team:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Tôi thuộc đội {self.name}")


player1 = Player("Palmer")
team1 = Team("Chelsea")

player1.introduce()
team1.introduce()

class Oto():
    def __init__ (self, hang, mau):
        self.hang = hang
        self.mau = mau

    def loaixe(self):
        print(f"Xe {self.hang} có màu {self.mau}")  
kieuxe = Oto("Toyota", "Đỏ")
print(kieuxe.hang)
print(kieuxe.mau)
loaixe = kieuxe.loaixe()

# Kế thừa
class Number:
    def Soduong(self):
        print("Số dương")
class Number1(Number):
    def Soam(self):
        print("Số âm nhỏ hơn số dương")
so = Number1()
so.Soduong()
so.Soam()
#Override
class Player:

    def introduce(self):
        print("Tôi là cầu thủ")
class ChelseaPlayer(Player):
    def introduce(self):
        print("Tôi là cầu thủ Chelsea")
player = ChelseaPlayer()
player.introduce()
# Mục đích override là muốn kế thừa hầu hết các phương thức của lớp cha, 
# nhưng muốn thay đổi một số phương thức cụ thể để phù hợp với nhu cầu của lớp con.
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Tôi là {self.name}")

    def run(self):
        print(f"{self.name} đang chạy")


class ChelseaPlayer(Player):
    def introduce(self):
        print(f"Tôi là {self.name}, cầu thủ Chelsea")

player = ChelseaPlayer("Thang", 11)
player.introduce()
player.run()

#Super() là gì
# Super() là một hàm được sử dụng trong lập trình hướng đối tượng để gọi phương
# thức hoặc thuộc tính của lớp cha từ lớp con. 
# Nó cho phép bạn truy cập và sử dụng các phương thức và thuộc tính của lớp cha 
# mà không cần phải viết lại mã.

class Player:
    def introduce(self):
        print("Tôi là cầu thủ nam")


class ChelseaPlayer(Player):
    def introduce(self):
        super().introduce()
        print("Tôi chơi cho Chelsea")
p = ChelseaPlayer()
p.introduce()
####super() với method trả về giá trị
class WC:
    def chauluc(self ):
       # self.name = name
        return "Palmer"
        print("Châu âu có 15 đội tham gia WC 2022")
class WC2022(WC):
    def chauluc(self):
        name = super().chauluc()
          
        return name +" "+"chelsea" 
wc = WC2022()
print(wc.chauluc())
###
class seagame:
    def vietnam(self, name, age ):
        self.name = name
        self.age = age
        print(f"Vận động viên tên {self.name} {self.age} tuổi")
vdv = seagame()
vdv.vietnam("Nguyen Tat Thang", 11)
### thêm arguments trước khi gọi super()
class Player:
    def introduce(self, name):
        print(f"Tôi là {name}")


class ChelseaPlayer(Player):
    def introduce(self, name):
        name = name.upper()
        super().introduce(name)
player = ChelseaPlayer()
player.introduce("Thang")
###xử lý kết quả từ super()
class Player:
    def get_position(self):
        return "RW"


class ChelseaPlayer(Player):
    def get_position(self):
        position = super().get_position()
        return position + " - Chelsea"

player = ChelseaPlayer()
print(player.get_position())
