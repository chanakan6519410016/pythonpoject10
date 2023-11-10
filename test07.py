import os

if os.path.exists('iotxx.txt') :
    os.remove('iotxx.txt')
else :
    print('File not found....^_^')