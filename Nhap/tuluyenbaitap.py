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



def add(a, b):
    return a + b
result = add(5, 3)
print(result)

#super cơ bản

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} tạo ra một âm thanh.")

class Dog(Animal):
    def __init__(self, name, breed):
        # 1. Gọi hàm __init__ của lớp Animal để thiết lập self.name
        super().__init__(name) 
        
        # 2. Khởi tạo thêm thuộc tính riêng của Dog
        self.breed = breed

    def speak(self):
        # Gọi lại hàm speak() của Animal
        super().speak() 
        # Thực thi thêm hành động riêng của Dog
        print(f"{self.name} sủa: Gâu gâu! (Giống: {self.breed})")

my_dog = Dog("Milu", "Corgi")
my_dog.speak()


