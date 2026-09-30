player_list = ["Palmer", "Caicedo", "James"]
player_list.append("Gusto")
print(player_list)
player = {"name": "Palmer", "age": 25, "position": "Forward"}
player["age"] = 26
print(player)
print(type(player_list))
print(type(player))
player.keys()
print(player.keys())
player.values()
print(player.values())
player.items()
print(player.items())
player.get("name")
print(player.get("age")) 
player_list.append("Pulisic")
print(player_list)
def chelsea(player):
    print("Chelsea player:", player)
chelsea("Palmer")

def create_player(name, age = 18, position="Midfielder"):
    player = {"name": name, "age": age, "position": position}
    return player
created_player = create_player("Palmer", 25, "Forward")
created_player2 = create_player("Caicedo", 24)
created_player3 = create_player("James")
print(created_player)
print(created_player2)
print(created_player3)
def stadium(*capacity):
    print(f"Số lượng khán giả: {capacity}")
stadium(50000)
stadium(60000, 70000)
def chelsea_players(**players):
    print(players)
###
chelsea_players(name = "Palmer", age=25, position="Forward")

class Ticket():
    def __init__(self, title, status="Mới"):
        self.title = title
        self.status = status
    def close(self):
        self.status = "Đã đóng"
dong = Ticket("Lỗi đăng nhập")
print(dong.title)
print(dong.status)
dong.close()
print(dong.status)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Xin chào {self.name}, bạn {self.age} tuổi.")
    def bye(self):
        print(f"Tạm biệt {self.name}, hẹn gặp lại!")
class Agent(User):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level
    def hello(self):
        print(f"Xin chào {self.name}, bạn {self.age} tuổi. Cấp độ: {self.level}.")
        super().hello()
        print("Chào mừng bạn đến với hệ thống.")

kh = Agent("Thang", 25, "Cao")
kh.hello()

def add(a, b):
    return a + b
result = add(5, 3)
print(result)
