GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m" 

print(f"{BOLD}{YELLOW}1. Gọi hàm khởi tạo của lớp cha".upper() + RESET)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) 
        self.student_id = student_id

hs = Student("Thang", 25, "HS001")
print(f"{CYAN}Tên:{RESET} {hs.name} | {GREEN}Tuổi:{RESET} {hs.age} | {YELLOW}Mã học sinh:{RESET} {hs.student_id}")
#2.Mở rộng (thay vì ghi đè hoàn toàn) một phương thức
print(f"{BOLD}{YELLOW}2. Mở rộng (thay vì ghi đè hoàn toàn) một phương thức".upper() + RESET)
class DataExporter:
    def export(self, data):
        print("Đang chuẩn bị dữ liệu...")
        print("Đang định dạng thành bảng...")

class PDFExporter(DataExporter):
    def export(self, data):
        # Gọi lại toàn bộ quá trình chuẩn bị của lớp cha
        super().export(data)
        
        # Chỉ viết thêm hành động đóng gói file PDF
        print("Đang xuất ra file PDF và đóng dấu bản quyền!")

pdf = PDFExporter()
pdf.export("Dữ liệu báo cáo")