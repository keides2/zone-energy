import csv
import networkx as nx
import matplotlib.pyplot as plt
import itertools as itr

path = '/Users/keisu/Documents/GitHub/zone-energy/'
path_1 = '/Users/keisu/Documents/GitHub/zone-energy/50-500.txt'
path_2 = '/Users/keisu/Documents/GitHub/zone-energy/q3-sample.txt'
path_3 = '/Users/keisu/Documents/GitHub/zone-energy/5-94.txt'
path_4 = '/Users/keisu/Documents/GitHub/zone-energy/6-16.txt'

# データファイルオープン
with open(path_2) as f:
    reader = csv.reader(f, delimiter=' ')
    nodes_list = [row for row in reader]

# 結果ファイルオープン
f = open(path + 'result.txt', 'w')

print("nodes_list: ", nodes_list)
# 6-16.txt の場合
# nodes_list: [['6', '16'], ['0', '1'], ['0', '2'], ... , ['4', '3'], ['4', '5'], ['5', '4']]
# 6 nodes, 8 edges (重複なし), 16 edges (重複あり、16行)
s = "nodes_list: " + str(nodes_list) + '\n'
f.write(s)

# nodes list, start with nodes_list[1]
del nodes_list[0]
print("new nodes_list: ", nodes_list)
# nodes_list: [['0', '1'], ['0', '2'], ... , ['4', '3'], ['4', '5'], ['5', '4']]
s = "nodes_list: " + str(nodes_list) + '\n'
f.write(s)

# Graphオブジェクトの作成
G = nx.Graph()

# リストからまとめてnodeを追加
for node_pair in nodes_list:
    print("node_pair: ", node_pair)
    # node_pair:  ['0', '1']
    s = "node_pair: " + str(node_pair) + '\n'
    f.write(s)
    G.add_nodes_from(node_pair)

print("★Nodes: ", G.nodes())
# Nodes:  ['0', '1', '2', '3', '4', '5']
s = "Nodes: " + str(G.nodes()) + '\n'
f.write(s)

# edgeを追加。有向グラフなので1つ目の引数がstart、2つ目の引数がtarget
for node_start, node_target in nodes_list:
    print("node_start: %s, node_target: %s" % (node_start, node_target))
    # node_start: 0, node_target: 1
    s = "node_start: " + str(node_start) + ',' + "node_target: " + str(node_target) + '\n'
    f.write(s)
    G.add_edge(node_start, node_target)

print("★Edges: ", G.edges())
# ★Edges:  [('0', '1'), ('0', '2'), ('1', '2'), ('1', '3'), ('2', '3'), ('2', '4'), ('3', '4'), ('4', '5')]
s = "Edges: " + str(G.edges()) + '\n'
f.write(s)

s = "---" + '\n'
f.write(s)

# Graphオブジェクトの情報
print("Info: ", nx.info(G))
'''
Info:  Name:
Type: Graph
Number of nodes: 6
Number of edges: 8
Average degree:   2.6667
'''
s = "Info: " + str(nx.info(G)) + '\n'
f.write(s)

# nodeの総数
print("G.number of nodes:", G.number_of_nodes())    # 6
s = "G.number of nodes: " + str(G.number_of_nodes()) + '\n'
f.write(s)

# nodeの要素一覧
print("G.nodes:", G.nodes())    # ['0', '1', '2', '3', '4', '5']
s = "G.nodes: " + str(G.nodes()) + '\n'
f.write(s)

# edgeの総数
print("G.number of edges:", G.number_of_edges())    # 8
s = "G.number of edges: " + str(G.number_of_edges()) + '\n'
f.write(s)

# edgeの要素一覧
print("G.edges:", G.edges())
# [('0', '1'), ('0', '2'), ('1', '2'), ('1', '3'), ('2', '3'), ('2', '4'), ('3', '4'), ('4', '5')]
s = "G.edges: " + str(G.edges()) + '\n'
f.write(s)

# 次数（nodeが持つedgeの数 = 重複あり）
print("G.degree:", G.degree())
#  [('0', 2), ('1', 3), ('2', 4), ('3', 3), ('4', 3), ('5', 1)]
# 合計すると 16
s = "G.degree: " + str(G.degree()) + '\n'
f.write(s)

# 指定したノードに対する、隣接しているノードの数
print("Node: '%s', Degree: %d" % ('0', G.degree('0')))
# Node: '0', Degree: 2
s = "Node: " + "'0' " + str(G.degree('0')) + '\n'
f.write(s)

# 指定したノードに対する、隣接しているノードの一覧
print("nx.all_neighbors: ", list(nx.all_neighbors(G, '0')))
#  ['1', '2']
s = "nx.all_neighbors: " + str(list(nx.all_neighbors(G, '0'))) + '\n'
f.write(s)

# ノードと隣接しているノードの数
for node in G.nodes():
    print("Node %s, G.degree(隣接しているノードの数) %d" % (node, G.degree(node)))
    '''
    Node 0, G.degree(隣接しているノードの数) 2
    Node 1, G.degree(隣接しているノードの数) 3
    Node 2, G.degree(隣接しているノードの数) 4
    Node 3, G.degree(隣接しているノードの数) 3
    Node 4, G.degree(隣接しているノードの数) 3
    Node 5, G.degree(隣接しているノードの数) 1
    '''
    s = "Node " + str(node) + ", G.degree(隣接しているノードの数) " + str(G.degree(node)) + '\n'
    f.write(s)

# 15C3 組み合わせ
nodes = G.nodes()   # ['0', '1', '2', '3', '4', '5']
print("Sum of combinations(nＣ3 組み合わせ総数): ", len(list(itr.combinations(nodes, 3))))  # 20
s = "Sum of combinations(nＣ3 組み合わせ総数): " + str(len(list(itr.combinations(nodes, 3)))) + '\n'
f.write(s)

s = "---" + '\n'
f.write(s)

# 15C3 組み合わせ総当たり
count_max = 0
node_0 = ''
node_1 = ''
node_2 = ''

# 15C3
for x in itr.combinations(nodes, 3):
    print("x: ", x)
    #('0', '1', '2')
    node_0, node_1, node_2 = x
    # node_0 = x[0]
    # node_1 = x[1]
    # node_2 = x[2]

    # 既出ノードのリスト
    exist_node = []

    nodes = G.nodes()
    print("nodes: ", nodes)
    # ['0', '1', '2', '3', '4', '5']

    # このリストを使う。使った要素は除く
    edges = G.edges()
    print("edges: ", edges)
    # [('0', '1'), ('0', '2'), ('1', '2'), ('1', '3'), ('2', '3'), ('2', '4'), ('3', '4'), ('4', '5')]
    list_edges = []
    for x in edges:
        y = list(x)
        list_edges.append(y)
    print(list_edges)
    # [['0', '1'], ['0', '2'], ['1', '2'], ['1', '3'], ['2', '3'], ['2', '4'], ['3', '4'], ['4', '5']]

    degrees = G.degree()
    print("degrees: ", degrees)
    # [('0', 2), ('1', 3), ('2', 4), ('3', 3), ('4', 3), ('5', 1)]
    list_degrees = []
    for x in degrees:
        y = list(x)
        list_degrees.append(y)
    print(list_degrees)
    # [['0', 2], ['1', 3], ['2', 4], ['3', 3], ['4', 3], ['5', 1]]

    count_0 = 0
    count_1 = 0
    count_2 = 0
    del_list = []
    print("len(list_edges): ", len(list_edges))

    for i in range(len(list_edges)):
        if node_0 in list_edges[i][0]:
            del_list.append(i)
            list_edges[i] = ['z', 'z']
            count_0 += 1
        if node_0 in list_edges[i][1]:
            del_list.append(i)
            list_edges[i] = ['z', 'z']
            count_0 += 1

    print("del_list: ", del_list)

    print(1)
    print("list_edges: ", list_edges)
    print(count_0, count_1, count_2)

    del_list =[]
    print("len(list_edges): ", len(list_edges))
    for i in range(len(list_edges)):
        if node_1 in list_edges[i][0]:
            del_list.append(i)
            list_edges[i] = ['z', 'z']
            count_1 += 1
        if node_1 in list_edges[i][1]:
            del_list.append(i)
            list_edges[i] = ['z', 'z']
            count_1 += 1

    print("del_list: ", del_list)

    print(2)
    print("list_edges: ", list_edges)
    print(count_0, count_1, count_2)

    del_list =[]
    print("len(list_edges): ", len(list_edges))
    for i in range(len(list_edges)):
        if node_2 in list_edges[i][0]:
            del_list.append(i)
            list_edges[i] = ['z', 'z']
            count_2 += 1
        if node_2 in list_edges[i][1]:
            del_list.append(i)
            list_edges[i] = ['z', 'z']
            count_2 += 1

    print(3)
    print("list_edges: ", list_edges)
    print(count_0, count_1, count_2)

    sum_count = count_0 + count_1 + count_2
    print("sum_count: ", sum_count)

    if count_max < sum_count:
        count_max = sum_count
        node_0_max = node_0
        node_1_max = node_1
        node_2_max = node_2

        s = '\nMax:'
        f.write(s)
        s = '(' + node_0_max + ', ' + node_1_max + ', ' + node_2_max + ') : ' + 'Sum: ' + str(count_max) + '\n'
        f.write(s)

print(node_0_max, node_1_max, node_2_max, count_max)
s = 'Result: ' + node_0_max + ' ' + node_1_max + ' ' + node_2_max + ' ' + 'Sum: ' + str(count_max) + '\n'
f.write(s)
f.close()

# ネットワークの可視化
nx.draw(G, with_labels = True, node_size = 200)
plt.show()
