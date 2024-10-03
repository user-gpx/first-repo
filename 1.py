import numpy as np
import os
import re

#将npy文件转换为txt文件
exp_dir = "modelnet40_c\label.npy"
loaded_arr = np.load(exp_dir)
np.set_printoptions(threshold=np.inf)   #设置打印的最大行数为无限 只用设置一次就行

print("start")
with open('laebl_output.txt', 'w') as f:
    for row in loaded_arr:
        f.write(str(row) + '\n')
print(loaded_arr.shape)
print("end")

# #读取label.txt文件中的数字 确实是代表类别
# numbers=set()
# with open('laebl_output.txt', 'r') as f:
#     for line in f:
#         match = re.search(r'\[(\d+)\]', line) 
#          #\[表示匹配[，\d表示匹配数字，+表示匹配一个或多个数字， \]表示匹配]  用\转义 ()表示提取括号内的内容并返回给match
#         if match: 
#             # 提取数字并添加到集合中
#             numbers.add(int(match.group(1)))
# print("找到的数字:", sorted(numbers))

exp_dir = "modelnet40_c"
#获取文件夹中的文件名   
files = os.listdir(exp_dir) #得到文件夹下的所有文件名称 是个列表
# with open('class_output.txt', 'w') as f:
#     for file in files:
#         f.write(file + '\n')

for file in files:
    if(file=='label.npy'):
        continue
    if(file=='.DS_Store'):
            continue
    print(file)
    loaded_arr = np.load(exp_dir+'/'+file)
    np.set_printoptions(threshold=np.inf) #可有可无
    save_path=file.replace('.npy','') +'.txt'#去掉.npy
    if(os.path.exists(save_path)):
        print("文件已存在")
        continue
    with open(save_path, 'w') as f:
        for row in loaded_arr:
               f.write(str(row) + '\n') 
    print(loaded_arr.shape)








