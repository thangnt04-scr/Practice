#1.Viết class Ticket thuần Python có thuộc tính title , status ,
#method close() .
print("1. Viết class Ticket thuần Python có thuộc tính title , status , method close()".upper() )
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
#2.Viết class Agent kế thừa từ class User , override 1 method và gọi super()
print("2. Viết class Agent kế thừa từ class User , override 1 method và gọi super()".upper() )
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

def tinh_giai_thua(n):
    if n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

print(tinh_giai_thua(5))  # Kết quả: 120