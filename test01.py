# Exception HandIing
# ข้อผิดพลาด การจัดการ
# Exception ข้อผิดพลาดที่เกิดขึ้นตอนโปๆรแแกรมทำงาน
# try-exception-finally

try :
    num1 = int( input('ป้อนตัวเลขที่ 1 :'))
    num2 = int( input('ป้อนตัวเลขที่ 2 :'))

    sum = num1 + num2
    result = num1 / num2

    print(f'ผลรวมของ{num1} + {num2} คือ {sum}')
    print(f'ผลรวมของ{num1} / {num2} คือ {result}')
except ValueError :
    print('ป้อนตัวเลขเท่านั้นห้ามป้อนตัวอักษร.......สงสัยติดต่อ  IT')
except ZeroDivisionError :
    print('ป้อนตัวเลขตัวที่ 2 ห้ามเป็น 0.......สงสัยติดต่อ  IT')
except Exception :
    print('มีข้อผิดพลาดเกิดขึ้น ต้องขอประทานอภัยอย่างสูง ช่วยติดต่อ IT ด้วยจะแก้ให้')
finally :
    print('Wow...')
    print('Hello...')
