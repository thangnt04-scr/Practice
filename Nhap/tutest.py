class Ticket():
    def close(self, ticket, status):
        self.ticket = ticket
        self.status = status
        return f"Ticket: {self.ticket}, Trạng thái: {self.status}"
trangthai = Ticket()
print(trangthai.close("Gọi hỗ trợ", "Open"))  

class User:
    def nguoidung(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        print("Người hỗ trợ là:")
        return f"{self.name} - {self.age} tuổi - vai trò: {self.role}"
class Agent(User):
    def nguoidung(self, name, age, role):
        super().nguoidung(name, age)
        self.role = role
     
nd = Agent()

nd.nguoidung("Thang", 25, "Admin")

print(nd.info)


    