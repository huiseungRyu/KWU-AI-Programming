
array = [[ 0 for col in range(15)] for row in range(31)]
my_dict_by_name={}
my_dict_by_index={}
names=[0 for names_length in range(31)]
idxs=[0 for idx_len in range(15)]
bool_name=False
bool_index=False

def input_list():
    num=[]
    while True:
        input_data = input("이름, 항목 혹은 이름과 항목 모두 입력하시오(입력을 끝냈으면 아무값도 없이 엔터키 입력) :")
        if input_data == '':
            break
        else:
            num.append(input_data)
    return num

def name_index_input(input_data):
    i=0
    x=input_data[0]
    y=input_data[-1]

    #행(이름)
    for j in range(31):
        if  x==names[j]:
            bool_name=True
            break
        elif y==names[j]:
            bool_name=True
            break
        else:
            bool_name=False 
    #열(항목)
    for k in range(15):
        if x==idxs[k]:
            bool_index=True
            break
        elif y==idxs[k]:
            bool_index=True
            break
        else:
            bool_index=False
    return j,k,bool_name, bool_index        
            
#파일 오픈
f = open('C:/Users/rs555/Desktop/AIProgramming/hw2.csv', 'r', encoding = 'UTF-8-sig')

i=0
while True:
    line=f.readline()
    array.insert(i,line.split(','))
    i=i+1
    if not line:
        break

for i  in range(0,31):
    array[i][14]=array[i][14].replace('\n',"")

#이름 저장
for i in range(0,31):
    names[i]=array[i][0]
#인덱스 저장
for id in range(15):
    idxs[id]=array[0][id]
#데이터 입력
input_data=input_list()

j,k, bool_name, bool_index=name_index_input(input_data)

if (bool_name==True)&(bool_index==False): #name만 입력
    #print('only name true')
    for row in range(1,15):
        my_dict_by_name[array[0][row]]=list(array[j][row].split(','))
    print(my_dict_by_name.items())

elif (bool_name==False)&(bool_index==True): #index만 입력
    #print('index true')
    for col in range(1,31):
        my_dict_by_index[array[col][0]]=list(array[col][k].split(','))
    sorted_dict = sorted(my_dict_by_index.items(), key = lambda item:item[1], reverse=True)
    print(sorted_dict)

elif (bool_name==True)&(bool_index==True): #name, index 모두 입력
    #print('both true')
    print(array[j][k])
    
else:
    print('입력값이 잘못되었습니다. 다시 입력해주세요')

f.close()



