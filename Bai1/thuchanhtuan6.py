# OOP
# Phần A
class bai1A ():
    def __init__ (self,cd,cr):
        self.cd = cd
        self.cr = cr
    def dt (self):
        return self.cd * self.cr

class shape ():
    def __init__ (self):
        pass
    def get_area (self):
        return 0
class square (shape):
    def __init__ (self,len):
        self.len = len
    def get_area (self):
        return self.len ** 2
    
# Phần B
class student ():
    score = []

    def __init__ (self,name,number):
        self.name = name
        for i in range(len(self.score)):
            self.score[i] = 0
        self.number = number
    
    def getName (self):
        return self.name
    
    def getScore (self):
        for i in range(self.number):
            print("Score ",i+1,": ",self.score[i])
    
    def inputScore (self):
        for i in range(self.number):
            value = input(f"Nhập vào điểm thứ %d: " %(i+1))
            self.score.append(value)
    def get_AVG (self):
        cnt = 0
        sum = 0.0
        for i in range (self.number):
            sum += float(self.score[i])
            cnt += 1
        res = sum/cnt
        print(f"Điểm trung bình của thí sinh: {res}") 
    def get_high_score (self):
        print(max(self.score,key = float))
    def get_AVG_value (self):
        cnt = 0
        sum = 0.0
        for i in range (self.number):
            sum += float(self.score[i])
            cnt += 1
        res = sum/cnt
        return res
    def get_Collegus_score (self):
        value = self.get_AVG_value()
        print(value)
        for i in range(self.number):
            if (float(self.score[i]) > 4.0 and float(value) >= 8.0):
                print("Bạn được nhận học bổng!!!")
                break
            else:
                print("Bạn không được nhận học bổng :(((")
                break
    def __repr__(self) -> str:
        return f'student(name={self.getName()},môn thi={self.number})'
        
class complexNumber ():
    def __init__ (self,thuc,ao):
        self.thuc = thuc
        self.ao = ao
    def chuyenAo (self):
        self.ao *= -1
        return self.ao
    def __repr__(self) -> str:
        # if (int(self.ao) > 0):
            return f'z = {self.thuc}+{self.ao}i'
        # else:
        #     res_ao = self.chuyenAo()
        #     return f'z = {self.thuc}-{res_ao}i'
    def input (self):
        pass
    def my_add (self,other):
        res_thuc = int(self.thuc) + int(other.thuc)
        res_ao = int(self.ao) + int(other.ao)
        print(f"{res_thuc},{res_ao}")
    def my_sub (self,other):
        res_thuc = self.thuc - other.thuc
        res_ao = self.ao - other.ao
        print(f"{res_thuc},{res_ao}")
    def my_mul (self,other):
        res_thuc = self.thuc * other.thuc
        res_ao = self.ao * other.ao
        print(f"{res_thuc},{res_ao}")
    def my_div (self,other):
        res_thuc = self.thuc / other.thuc
        res_ao = self.ao / other.ao
        print(f"{res_thuc},{res_ao}")
    def __add__ (self,other):
        res_thuc = int(self.thuc) + int(other.thuc)
        res_ao = int(self.ao) + int(other.ao)
        return complexNumber(res_thuc,res_ao)
    def __sub__ (self,other):
        res_thuc = self.thuc - other.thuc
        res_ao = self.ao - other.ao
        return complexNumber(res_thuc,res_ao)
    def __mul__ (self,other):
        res_thuc = self.thuc * other.thuc
        res_ao = self.ao * other.ao
        return complexNumber(res_thuc,res_ao)
    def __truediv__ (self,other):
        res_thuc = self.thuc // other.thuc
        res_ao = self.ao // other.ao
        return complexNumber(res_thuc,res_ao)
    def length (self):
        return (int(self.thuc)**2 + int(self.ao)**2)**0.5
    def compare (self,other):
        return (self.thuc == other.thuc and self.ao == other.ao)
    def __eq__ (self,other):
        return (self.length() == other.length())
    def __lt__ (self,other):
        return (self.length() < other.length())
    def __gt__ (self,other):
        return (self.length() > other.length())
class complexNumber2 (complexNumber):
    def __init__ (self):
        self.thuc = 0
        self.ao = 0
    def input (self):
        self.thuc = input("Nhập vào phần thực: ")
        self.ao = input("Nhập vào phẩn ảo: ")
    def __repr__(self) -> str:
        return super().__repr__()
    
class PhanSo (object):
    def __init__ (self,mau,tu):
        self.mau = mau
        self.tu = tu
    def ucln (self):
        soMax = max(int(self.mau),int(self.tu))
        arr = []
        for i in range(1,soMax+1):
            if (int(self.mau)%i==0 and int(self.tu)%i==0):
                arr.append(i)
        uc = max(arr,key=int)
        return uc
    def rutgon (self):
        self.tu //= self.ucln()
        self.mau //= self.ucln()
        return self.tu + "/" + self.mau
    def __str__ (self):
        self.tu //= self.ucln()
        self.mau //= self.ucln()
        print(f'{self.tu}/{self.mau}')
    def nghichDao (self):
        temp = int(self.tu)
        self.tu = self.mau
        self.mau = temp
        print(f'{self.tu}/{self.mau}')
    def my_add (self):
        res_tu = int(self.tu) + int(self.mau)
        res_mau = int(self.mau) + int(self.mau)
        print(f'{self.tu}/{self.mau}')
    def my_sub (self):
        res_tu = int(self.tu) - int(self.mau)
        res_mau = int(self.mau) - int(self.mau)
        print(f'{self.tu}/{self.mau}')
    def my_mul (self):
        res_tu = int(self.tu) * int(self.mau)
        res_mau = int(self.mau) * int(self.mau)
        print(f'{self.tu}/{self.mau}')
    def my_div (self):
        res_tu = int(self.tu) / int(self.mau)
        res_mau = int(self.mau) / int(self.mau)
        print(f'{self.tu}/{self.mau}')
    def __add__ (self, other):
        res_tu = int(self.tu) + int(self.mau)
        res_mau = int(self.mau) + int(self.mau)
        return PhanSo(res_tu,res_mau)
    def __sub__ (self, other):
        res_tu = int(self.tu) - int(self.mau)
        res_mau = int(self.mau) - int(self.mau)
        return PhanSo(res_tu,res_mau)
    def __mul__ (self, other):
        res_tu = int(self.tu) * int(self.mau)
        res_mau = int(self.mau) * int(self.mau)
        return PhanSo(res_tu,res_mau)
    def __truediv__ (self,other):
        res_tu = int(self.tu) / int(self.mau)
        res_mau = int(self.mau) / int(self.mau)
        return PhanSo(res_tu,res_mau)

class Shape(object):
    def __init__ (self,color,name):
        self.color = color
        self.name = name
    def findarea (self):
        pass
    def findperimeter (self):
        pass
    def __str__(self) -> str:
        return self.name
    
class Circle (Shape):
    def __init__(self, color, name,radius):
        super().__init__(color, name)
        self.radius = radius
    def findarea (self):
        import math
        area = math.pi * (self.radius ** self.radius)
        return area
    def findperimeter (self):
        import math
        c = math.pi * 2 * self.radius
        return c

class Rectangle (Shape):
    def __init__(self,color,name,width,height):
        super().__init__(color,name)
        self.width = width
        self.height = height
    def findarea (self):
        return self.width * self.height
    def findperimeter(self):
        return (self.width + self.height) * 2

class Square (Rectangle):
    def __init__(self, color, name, width, height):
        super().__init__(color, name, width, height)
    def findarea(self):
        if (self.width == self.height):
            return self.width * self.height
        else:
            return super().findarea(self)
    def findperimeter(self):
        return self.width * 4


class Employee(object):

    def __init__(self,id,fullName,birth,phone,email,employ_type) -> None:
        self.id = id
        self.fullName = fullName
        self.birth = birth
        self.phone = phone
        self.email = email
        self.employ_type = employ_type
    
    def input (self):
        self.id = input("Nhập vào id nhân viên: ")
        name = input("Nhập vào tên đầy đủ của nhân viên: ")
        if (checkError.checkTen(name)):
            self.fullName = name
        birthday = input("Nhập vào ngày sinh của nhân viên: ")
        if (checkError.checkTen(birthday)):
            self.birth = birthday
        phoneNumber = input("Nhập vào SĐT của nhân viên: ")
        if (checkError.checkPhone(phoneNumber)):
            self.phone = phoneNumber
        Email = input("Nhập vào email của nhân viên: ")
        if (checkError.checkEmail(Email)):
            self.email = Email
        value_type = input("Nhập vào vị trí nhân viên muốn ứng tuyển")
        if (value_type != "Intern" or value_type != "Fresher" or value_type != "Experience"):
            self.employ_type = value_type
        
    def show_infor (self):
        print(self.id," ",self.fullName," ",self.birthm," ",self.phone," ",self.email," ",self.employ_type)

class Experience (Employee):
    def __init__(self, id, fullName, birth, phone,employ_type, email,expYear,proSkill) -> None:
        super().__init__(id, fullName, birth, phone, email,employ_type)
        self.expYear = expYear
        self.proSkill = proSkill

    def input(self):
        super().input()
        self.expYear = input("Vui lòng nhập vào số năm kinh nghiệm: ")
        self.proSkill = input("Vui lòng nhập vào kỹ năng chuyên môn của bạn: ")

    def show_info(self):
        super().show_infor()
        print(self.expYear)
        print(self.proSkill)

    def getExpYear(self):
        return self.expYear

    def getProSkill(self):
        return self.proSkill
    
class Fresher (Employee):
    def __init__(self, id, fullName, birth, phone,employ_type,grad_date,grad_rank,eduplace):
        super().__init__(id, fullName, birth, phone,employ_type)
        self.grad_date = grad_date
        self.grad_rank = grad_rank
        self.eduplace = eduplace

    def get_gradDate (self):
        return self.grad_date
    
    def get_gradRank (self):
        return self.grad_rank
    
    def get_eduplace (self):
        return self.eduplace
    
    def input(self):
        super().input()
        self.grad_date = input("Vui lòng nhập vào ngày tốt nghiệp: ")
        self.grad_rank = input("Vui lòng nhập vào xếp loại tốt nghiệp: ")
        self.eduplace = input("Vui lòng nơi bạn học: ")

    def show_info(self):
        super().show_infor
        print(self.grad_date," ",self.grad_rank," ",self.eduplace)
    
class Intern (Employee):
    def __init__(self, id, fullName, birth, phone,employ_type,major,semes,uniName):
        super().__init__(id, fullName, birth, phone,employ_type)
        self.major = major
        self.semes = semes
        self.uniName = uniName
    
    def get_major (self):
        return self.major
    
    def get_semes (self):
        return self.semes
    
    def get_uniName (self):
        return self.uniName
    
    def input (self):
        super().input()
        self.major = input("Vui lòng nhập vào chuyên ngành bạn đang học: ")
        self.semes = input("Vui lòng nhập vào học kỳ bạn đang học: ")
        self.uniName = input("Vui lòng nhập vào tên trường bạn đang theo học: ")

    def show_info(self):
        super().show_infor()
        print(self.major," ",self.semes," ",self.uniName)



class checkError (object):

    @staticmethod
    def checkTen (name):
        import re
        if (len(name) >= 2):
            if re.search('0-9',name):
                return 'Your name can\'t containt numbers'
            else:
                if re.search('A-Za-z',name):
                    return True
                else:
                    return "Invalid Input!!!"
    
    @staticmethod
    def checkPhone (phone):
        if (len(phone) >= 10):
            if phone[0] == '0':
                return True
        return "Input Valid!!!"
    
    @staticmethod
    def checkEmail (email):
        if '@' in email and len(email) >= 7:
            return True
        else:
            return False
    
    @staticmethod
    def checkBirthday (birthday):
        import datetime
        try:
            datetime.datetime.strptime(birthday,'%d/%m/%Y')
        except ValueError:
            raise ValueError("Incorrect format, It may be YYYY-MM-DD")

class listEmployee ():
    def __init__(self):
        self.employ_cnt = 0
        self.list_employ = []
    
    def addEmploy(self):
        choice = input("Vui lòng nhập vào vị trí nhân viên cần thêm: ")
        if choice == 'Experience':
                nv = Experience()
                nv.input()
                self.employ_cnt += 1
                self.list_employ.append(nv)
        elif choice == 'Fresher':
                nv = Fresher()
                nv.input()
                self.employ_cnt += 1
                self.list_employ.append(nv)
        else:
                nv = Intern()
                nv.input()
                self.employ_cnt += 1
                self.list_employ.append(nv)
        
    def findAllExperience():
        for i in listEmployee:
            if isinstance(i,Experience):
                i.show_info()

    def findAllFresher():
        for i in listEmployee:
            if isinstance(i,Fresher):
                i.show_info()

    def findAllIntern():
        for i in listEmployee:
            if isinstance(i,Intern):
                i.show_info()