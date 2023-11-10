# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/extend (x)/append (x)/read (r)

f_iot = open('iot4.txt', 'a', encoding='utf-8')

f_iot.write('111....')
f_iot.write('222....\n')
f_iot.write('333...\n')

f_iot.close()

