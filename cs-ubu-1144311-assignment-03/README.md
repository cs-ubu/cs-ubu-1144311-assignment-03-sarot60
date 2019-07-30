# Assignment 03

สร้างเว็บเพื่อให้ผู้ใช้สามารถเรียกใช้ฟังก์ชันต่อไปนี้ผ่านเว็บได้

* แปลงเลขทศนิยมเป็น IEEE floating point single precision (32-bit)

```python
def decto32fp(d):
	pass
```

* แปลงเลขทศนิยมเป็น IEEE floating point double precision (64-bit)

```python
def decto32fp(d):
	pass
```

* แก้ระบบสมการเชิงเส้น $Ax = b$

```python
def solve(A, b):
	pass
```

## ขั้นตอนหลังการ clone มาใช้งาน
	
* ติดตั้ง `pipenv`

```sh
pip install pipenv
```

* เริ่มพัฒนา

```sh
cd hw03
pipenv shell --dev
```

* ปิดการใช้งาน `pipenv`

```sh
source deactivate
```

## ขั้นตอนการสร้าง project เอง

```sh
pip install pipenv
pipenv shell --three
pipenv install django
pipenv install djangorestframework
pipenv install django-cors-headers
django-amin startproject hw03
cd hw03 
python manage.py migrate
python manage.py startapp commathweb
```

