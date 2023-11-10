f_iot = open('iot4.txt', 'r', encoding='utf-8')

data = f_iot.readline()
print(data, end='') #ถ้าไม่อยากให้เว้นบรรทัดใส่ , end=''
data = f_iot.readline()
print(data, end='')
data = f_iot.readline()
print(data, end='')
data = f_iot.readline()
print(data, end='')

f_iot.close()