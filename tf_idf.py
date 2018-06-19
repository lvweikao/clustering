# coding=utf-8

import os
import codecs
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":

    #########################################################################
    #                           第一步 计算TFIDF

    # 文档预料 空格连接
    corpus = []

    # 读取预料 一行预料为一个文档
    for line in open('NewBaiduSpider.txt', 'r', encoding='UTF-8').readlines():
        print(line)
        corpus.append(line.strip())
    print(corpus, 'abc')
    print('\n' + corpus[0][22], 'abc')
    # time.sleep(1)

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()

    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()

    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    print('tfidf:')
    print(tfidf[0][0])
    print('/n')
    print('tfidf:')
    print(tfidf)
    print('/n')
    print('tfidf:')
    print(tfidf[29])
    print('/n')
    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()


    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()

    # 打印特征向量文本内容
    print('Features length: ' + str(len(word)))
    resName = "BHTfidf_Result.txt"
    result = codecs.open(resName, 'w', 'utf-8')
    for j in range(len(word)):
        result.write(word[j] + ' ')
    result.write('\r\n\r\n')

    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    zeroSum = 0
    unZero = [0] * 30
    for i in range(len(weight)):
        print("-------这里输出第", i, u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            # print weight[i][j],
            result.write(str(weight[i][j]) + ' ')
            # 判断为零的项有多少个
            if weight[i][j] == 0:
                zeroSum = zeroSum + 1
            # 记录各篇文章非零项个数
            if weight[i][j] != 0:
                unZero[i] = unZero[i] + 1
        result.write('\r\n\r\n')
    print('非零项的项数是：', 55350 - zeroSum)
    print('各篇文章的非零项是', unZero)

    result.close()

    ########################################################################
    #                               第二步 聚类Kmeans

    print('Start Kmeans:')
    from sklearn.cluster import KMeans
    # 设置中心点

    clf = KMeans(n_clusters=4, n_init=200, max_iter=1)
    s = clf.fit(weight)
    print(s, 'abc')
    print(len(clf.cluster_centers_[0]), 'abc')

    # 4个中心点
    print(clf.cluster_centers_, 'abc')

    # 每个样本所属的簇
    print(clf.labels_, 'abc')

    # 将这个分类结果存储
    fileName = "Cluster_Result.txt"
    if os.path.exists(fileName):
        os.remove(fileName)

    content = '1' + ' %d' % clf.labels_[0]
    i = 1
    while i <= len(clf.labels_) - 1:
        content = content + ('\n%d' % (i + 1)) + (' %d' % clf.labels_[i])
        i = i + 1
    # print(content)
    f = open("Cluster_Result.txt", 'wb')
    f.write(content.encode('UTF-8'))
    f.close()
    # 展示每个文档属于的簇
    i = 1
    while i <= len(clf.labels_):
        print(i, clf.labels_[i - 1])
        i = i + 1

    # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    print(clf.inertia_)