# -*- coding: UTF-8 -*-

MAX = float('inf')

matrix = [[0, 10, MAX, 4, MAX, MAX], [10, 0, 8, 2, 6, MAX],
          [MAX, 8, 10, 15, 1, 5], [4, 2, 15, 0, 6, MAX], [MAX, 6, 1, 6, 0, 12],
          [MAX, MAX, 5, MAX, 12, 0]]

# 矩阵一维数组的长度，即节点的个数
matrix_length = len(matrix)

# path = [start_node] * matrix_length
path = [[-1 for col in range(1)] for row in range(matrix_length)]


def indexToName(index):
    t = ["a", "b", "c", "d", "e", "f", "g"]
    return t[index]


def dijkstra(matrix, start_node):

    # 访问过的节点数组
    used_node = [False] * matrix_length

    # 最短路径距离数组
    distance = [MAX] * matrix_length

    # 初始化，将起始节点的最短路径修改成0
    distance[start_node] = 0

    for index in range(matrix_length):
        path[index] = [start_node]
    print('记录的数组为：', path)
    # 将访问节点中未访问的个数作为循环值，其实也可以用个点长度代替。
    loopCount = 0
    while used_node.count(False):
        min_value = float('inf')
        min_value_index = 999

        # 在最短路径节点中找到最小值，已经访问过的不在参与循环。
        # 得到最小值下标，每循环一次肯定有一个最小值
        for index in range(matrix_length):
            if not used_node[index] and distance[index] < min_value:
                min_value = distance[index]
                min_value_index = index

        print('选中的计算节点：', min_value_index, indexToName(min_value_index))
        # 将访问节点数组对应的值修改成True，标志其已经访问过了
        used_node[min_value_index] = True

        tempPath = path[min_value_index]

        # 更新distance数组。
        # 以B点为例：distance[x] 起始点达到B点的距离，
        # distance[min_value_index] + matrix[min_value_index][index] 是起始点经过某点达到B点的距离，比较两个值，取较小的那个。
        for index in range(matrix_length):
            p1 = distance[index]
            p2 = distance[min_value_index] + matrix[min_value_index][index]

            distance[index] = min(p1, p2)

            # print('比较 节点：', p2, p1, min_value_index, index)
            if ((p2 < p1)):
                # print('更新 001  ---', min_value_index, index)
                if (min_value_index == start_node):
                    path[index] = tempPath + [index]
                else:
                    path[index] = tempPath + [min_value_index, index]

                # print('更新节点路径-->', index, path[index])

        # print('第{0} 轮， 选中 index： {1} ,\n计算的结果： {2}\n'.format(
        # loopCount, min_value_index, distance))
        # print('更新记录为： ', used_node)
        # print('--节点 {0} -- 记录的路径为：{1}\n\n'.format(min_value_index, path))

        loopCount = loopCount + 1
    return distance


def getUniqueList(data):
    news_list = []
    for id in data:
        if id not in news_list:  # 当id不在news_list中就添加,在就不添加,达到去重的目的
            news_list.append(id)
    return news_list


def getPathName(data):
    news_list = []
    for id in data:
        news_list.append(indexToName(id))
    return news_list


start_node = int(input('请输入起始节点:'))
result = dijkstra(matrix, start_node)
print('结果->起始节点到其他点距离：%s' % result)

for i in range(len(path)):
    path[i] = getUniqueList(path[i])

for i in range(len(path)):
    path[i] = getPathName(path[i])

print('记录的路径为：', path)
