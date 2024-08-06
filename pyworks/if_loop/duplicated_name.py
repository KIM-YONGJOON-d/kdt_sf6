# 리스트, 셋을 사용 - 중복 이름 찾기
name = ["흥부", "콩쥐", "놀부", "콩쥐"]
duplicated_name = set() #빈 셋을 생성
# duplicated_name = []
n= len(name)

for i in range(0, n-1):
    for j in range(i+1, n):
        if name[i]== name[j]:
            duplicated_name.add(name[i])
            #uplicated_name.append(name[i])


'''
    i=0, j=1, name[0] == name[1] "흥부" == "콩쥐"
         j=2, name[0] == name[2] "흥부" == "놀부"
         j=3, name[0] == name[3] "흥부" == "콩쥐"
    i=1, j=2, name[1] == name[2] "콩쥐" == "놀부"
         j=3, name[1] == name[3] "콩쥐" == "콩쥐"
'''

print(f'중복 이름: {duplicated_name}')