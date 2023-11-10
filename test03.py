# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/extend (x)/append (x)/read (r)
try :    
    f_iot = open('iot4.txt', 'x', encoding='utf-8')

    f_iot.write('Wow....')
    f_iot.write('Hi....\n')
    f_iot.write('สวัสดี...\n')

    f_iot.close()
except FileExistsError :
    print('กรุณาเปลี่ยนชื่อไฟล์ใหม่เพราะซ้ำ...')
