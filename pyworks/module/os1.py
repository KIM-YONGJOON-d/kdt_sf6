# os모듈 - 디렉터리, 파일 등의 자원을 제어하는 모듈이다
import os
file_path = os.chdir("c:/KDT_SF6/pyworks/module")

dir = os.popen('dir')
print(dir.read())

print(os.listdir(file_path))