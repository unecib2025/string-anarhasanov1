#1
name=input("Введите имя: ")
name=name.strip()
if name.isalnum():
    name=name.lower()
    print("Имя корректно")
else:
    print("Ошибка")

#2
password=input("Введите пароль: ")
length=len(password)>=8
digit=False
upper=False
for s in password:
    if s.isdigit():
        digit=True
    if s.isupper():
        upper=True
if length and digit and upper:
    print("Пароль надёжен")
else:
    print("Пароль слаб")

#3
log="ACCESS DENIED"
a=log.capitalize()+"–вход запрещён"
print(a)

#4
data="ERROR connection ERROR failed access"
data=data.replace("ERROR", "ALERT")
s=data.count("ALERT")
print(data, s)

#5
email=input("Введите email: ")
if email.find("@") != -1:
    a=email.split("@")
    username=a[0]
    domain=a[1]
    print("Домен:", domain)
else:
    print("Некорректный адрес")

#6
a=input()
a=a.strip()
a=a.lower()
a=a.replace(" ","_")
print(a)

#7
a=input()
if a.find("SECRET")!=-1:
    a=a.replace("SECRET","******")
    print("Обнаружено секретная информация")
else:
    print("Безопасно")

#8
a=input("Введите слово: ")
b=""
for c in a:
    b+=str(ord(c))+" "
print("Коды символов:", b.strip())
d=""
for c in a:
    d+= chr(ord(c))
print(d)

#9
text="login attempt failed access denied unauthorized access"
a=text.count("failed")
b=text.count("denied")
if a>0 or b>0:
    print("Попытка несанкционированного доступа")

#10
a=input("Введите текст отчёта: ")
s=a.split(".")
s=len(s)-1
print("Количество предложений:",s)
b=len(a.replace(" ",""))
print("Количество символов без пробелов:",b)
if a.lower().startswith("report"):
    print("Текст начинается с 'Report'")
else:
    print("Текст не начинается с 'Report'")
if a.lower().count("error")>=2:
    print("Ошибки найдены")
else:
    print("Ошибок нет")
