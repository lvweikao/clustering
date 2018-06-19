# coding=utf-8
import os
import sys
import codecs

'''
功能:合并实体名称和聚类结果 共类簇4类
输入:BH_EntityName.txt Cluster_Result.txt
输出:ZBH_Cluster_Merge.txt ZBH_Cluster_Result.txt
'''

source1 = open("D:\PYC/textClustering\clustering/baiduSpider/Catalog.txt", 'r', encoding='UTF-8')
source2 = open("Cluster_Result.txt", 'r', encoding='UTF-8')
result1 = codecs.open("ZBH_Cluster_Result.txt", 'w', encoding='UTF-8')

#########################################################################
#                        第一部分 合并实体名称和类簇

lable = []  # 存储30个类标 4个类
content = []  # 存储30个实体名称
name = source1.readline()

while name != "":
    name = name.strip('\r\n')
    print(name, 'abc')
    res = source2.readline()
    res = res.strip('\r\n')
# 以空格为基准进行切片
    value = res.split(' ')
    print(value, 'abc1')
    no = int(value[0]) - 1  # 行号
    va = int(value[1])  # 值
    lable.append(va)
    content.append(name)
    print(name, res)
    result1.write(name + ' ' + res + '\r\n')
    name = source1.readline()

else:
    print('OK')
    source1.close()
    source2.close()
    result1.close()

# 测试输出 其中实体名称和类标一一对应
i = 0
while i < len(lable):
    print(content[i], (i + 1), lable[i])
    i = i + 1

#########################################################################
#                      第二部分 合并类簇 类1 ..... 类2 .....

# 定义定长30字符串数组 对应4个类簇
output = [''] * 4
result2 = codecs.open("ZBH_Cluster_Merge.txt", 'w', 'utf-8')

# 统计类标对应的实体名称
i = 0
while i < len(lable):
    output[lable[i]] += content[i] + ' '
    i = i + 1

# 输出
i = 0
while i < 4:
    print('#######')
    result2.write('#######\r\n')
    print('Label: ' + str(i))
    result2.write('Label: ' + str(i) + '\r\n')
    print(output[i])
    result2.write(output[i] + '\r\n')
    i = i + 1

result2.close()