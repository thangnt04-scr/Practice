# def hello():
#     print("Hello, world!")

# def decarator_example(hello):
#     def wrapper():
#         print("Before the function is called.")
#         hello()
#         print("After the function is called.")
#     return wrapper
# @decarator_example
# def hello():
#     print("Hello, world!")
# hello()


# @property
class NhanVien:
    def __init__(self, luong):
        self._luong = luong  # Biến private (quy ước có dấu gạch dưới)

    # 1. Getter
    @property
    def luong(self):
        return self._luong

    # 2. Setter
    @luong.setter
    def luong(self, gia_tri_moi):
        if gia_tri_moi < 0:
            raise ValueError("Lương không thể là số âm!")
        self._luong = gia_tri_moi

nhan_vien = NhanVien(1000)
print(nhan_vien.luong)     # Truy cập như thuộc tính: 1000 (Không cần nhan_vien.luong())
nhan_vien.luong = -500     # Gọi tới setter
# nhan_vien.luong = -500   # Sẽ báo lỗi ValueError

# class Player:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @property
#     def info(self):
#         return f"{self.name} - {self.age}"
# player = Player("Thang", 25)
# print(player.info)  # Sử dụng property để truy cập thông tin của player
