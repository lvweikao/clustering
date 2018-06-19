# coding=utf-8
import os
import codecs

# 这里加载停用词的路径
stopwords = open("D:\PYC/textClustering\clustering/stopwords.txt", 'r', encoding='utf-8').readlines()
k = 0
while k < len(stopwords):
    stopwords[k] = stopwords[k].strip('\r\n ')
    k += 1
print(stopwords)
def delete_stop(word):
    return word not in stopwords
def merge_file():
    path = "NewBaiduSpider\\"
    resName = "NewBaiduSpider.txt"
    if os.path.exists(resName):
        os.remove(resName)
    result = codecs.open(resName, 'w', 'utf-8')

    num = 1
    while num <= 30:
        name = "%04d" % num
        fileName = path + str(name) + ".txt"
        source = open(fileName, 'r', encoding='UTF-8')
        line = source.readline()
        line = line.strip('\n')
        line = line.strip('\r')

        while line != "":
            line = line.replace('\n', ' ')
            line = line.replace('\r', ' ')
        # 下面对line进行去除停用词操作
            # 将每一行的值切片成序列
            value = line.split(' ')
            newvalue = filter(delete_stop, value)
            line = ''
            for word in newvalue:
                line += word + ' '
        # 去除完停用词将结果写入result中
            result.write(line)
            line = source.readline()
        else:
            print('End file: ' + str(num))
            result.write('\r\n')
            source.close()
        num = num + 1

    else:
        print('End All')
        result.close()


if __name__ == '__main__':
    merge_file()