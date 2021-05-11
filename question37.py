import csv
import networkx as nx
import matplotlib.pyplot as plt
import itertools as itr

path = '/Users/keisu/Documents/GitHub/zone-energy/'
path_1 = '/Users/keisu/Documents/GitHub/zone-energy/50-500.txt'
path_2 = '/Users/keisu/Documents/GitHub/zone-energy/q3-sample.txt'
path_3 = '/Users/keisu/Documents/GitHub/zone-energy/5-94.txt'
path_4 = '/Users/keisu/Documents/GitHub/zone-energy/6-16.txt'
path_5 = '/Users/keisu/Documents/GitHub/zone-energy/6-30.txt'

# データファイルオープン
with open(path_1) as f:
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
s = "new nodes_list: " + str(nodes_list) + '\n'
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
s = "\n★Nodes: " + str(G.nodes()) + '\n'
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
s = "\n★Edges: " + str(G.edges()) + '\n'
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
print("Node exsample: '%s', Degree: %d" % ('0', G.degree('0')))
# Node: '0', Degree: 2
s = "Node example: " + "'0' " + str(G.degree('0')) + '\n'
f.write(s)

# 指定したノードに対する、隣接しているノードの一覧
print("nx.all_neighbors of '0': ", list(nx.all_neighbors(G, '0')))
#  ['1', '2']
s = "nx.all_neighbors of '0': " + str(list(nx.all_neighbors(G, '0'))) + '\n'
f.write(s)

s = "---" + '\n'
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

#################################################
# nC3 組み合わせ
nodes = G.nodes()   # ['0', '1', '2', '3', '4', '5']
print("len(nodes): ", len(nodes))
s = "n=len(nodes): " + str(len(nodes)) + '\n'
f.write(s)

print("Sum of combinations(nＣ3 組み合わせ総数): ", len(list(itr.combinations(nodes, 3))))  # 20
s = "Sum of combinations(nＣ3 組み合わせ総数): " + str(len(list(itr.combinations(nodes, 3)))) + '\n'
f.write(s)

s = "---" + '\n'
f.write(s)

# nC3 組み合わせ総当たり
count_max = 0
node_0 = ''
node_1 = ''
node_2 = ''

nodes = G.nodes()
print("nodes: ", nodes)
# ['0', '1', '2', '3', '4', '5']
s = "nodes: " + str(nodes) + '\n'
f.write(s)

# このリストを使う。使った要素は除く
edges = G.edges()
print("edges: ", edges)
# [('0', '1'), ('0', '2'), ('1', '2'), ('1', '3'), ('2', '3'), ('2', '4'), ('3', '4'), ('4', '5')]
s = "edges: " + str(edges) + '\n'
f.write(s)

degrees = G.degree()
print("degrees: ", degrees)
# [('0', 2), ('1', 3), ('2', 4), ('3', 3), ('4', 3), ('5', 1)]
s = "degrees: " + str(degrees) + '\n'
f.write(s)

list_degrees = []
for x in degrees:
    y = list(x)
    list_degrees.append(y)
print(list_degrees)
# [['0', 2], ['1', 3], ['2', 4], ['3', 3], ['4', 3], ['5', 1]]
s = "list_degrees: " + str(list_degrees) + '\n'
f.write(s)

s = "---" + '\n'
f.write(s)

# 15C3
for x in itr.combinations(nodes, 3):
    print("x: ", x)
    #('0', '1', '2')
    s = "x: " + str(x) + '\n'
    f.write(s)

    node_0, node_1, node_2 = x
    # node_0 = x[0]
    # node_1 = x[1]
    # node_2 = x[2]
    print("node_0: ", node_0, type(node_0))

    # 既出ノードのリスト
    # exist_node = []

    # 出現回数
    count_0 = 0
    count_1 = 0
    count_2 = 0

    # 初期化
    get_node = []

    # node_0 のターゲットノードリスト
    # 指定したノードに対する、隣接しているノードの一覧
    node_0_nodes = list(nx.all_neighbors(G, node_0))
    print("node_0_nodes: ", node_0_nodes, type(node_0_nodes))
    #  ['1', '2']
    s = "node_0_nodes: " + str(node_0_nodes) + '\n'
    f.write(s)

    # node_1 のターゲットノードリスト
    # 指定したノードに対する、隣接しているノードの一覧
    node_1_nodes = list(nx.all_neighbors(G, node_1))
    print("node_1_nodes: ", node_1_nodes, type(node_1_nodes))
    #  ['0', '2', '3']
    s = "node_1_nodes: " + str(node_1_nodes) + '\n'
    f.write(s)

    # node_2 のターゲットノードリスト
    # 指定したノードに対する、隣接しているノードの一覧
    node_2_nodes = list(nx.all_neighbors(G, node_2))
    print("node_2_nodes: ", node_0_nodes, type(node_2_nodes))
    #  ['0', '1', '3', '4']
    s = "node_2_nodes: " + str(node_2_nodes) + '\n'
    f.write(s)

    # 取得済みノード一覧に、node_0 のターゲットノード一覧のノードが含まれていない場合、これを取得済みノード一覧に追加する
    for n in range(len(node_0_nodes)):
        # print("n: ", n)
        if node_0 != node_0_nodes[n]:
            get_node.append(node_0_nodes[n])

    print("get_node: ", get_node)   # ['1', '2']
    s = "get_node: " + str(get_node) + '\n'
    f.write(s)

    # 取得済みノード一覧に、node_1 のターゲットノード一覧のノードが含まれていない場合、これを取得済みノード一覧に追加する
    for n in range(len(node_1_nodes)):
        nothing = 0
        for m in range(len(get_node)):
            if node_1_nodes[n] != get_node[m]:
                # "not match"
                nothing += 1
            else:
                # "match"
                nothing = 0
                break
        if nothing > 0:
            # "append!"
            get_node.append(node_1_nodes[n])
        # else:
            # "not append!"

    print("get_node: ", get_node)   # ['1', '2', '0', '3']
    s = "get_node: " + str(get_node) + '\n'
    f.write(s)

    # 取得済みノード一覧に、node_2 のターゲットノード一覧のノードが含まれていない場合、これを取得済みノード一覧に追加する
    for n in range(len(node_2_nodes)):
        nothing = 0
        for m in range(len(get_node)):
            if node_2_nodes[n] != get_node[m]:
                # "not match"
                nothing += 1
            else:
                # "match"
                nothing = 0
                break
        if nothing > 0:
            # "append!"
            get_node.append(node_2_nodes[n])
        # else:
            # "not append!"

    print("get_node: ", get_node)   # ['1', '2', '0', '3', '4']
    s = "get_node: " + str(get_node) + '\n'
    f.write(s)

    s = "---" + '\n'
    f.write(s)

    # エッジ数の合計
    sum_count = len(get_node)
    print("sum_count(len(get_node)): ", sum_count)
    s = "sum_count(len(get_node)): " + str(sum_count) + '\n'
    f.write(s)

    # ここまでの最大値を更新
    if count_max <= sum_count:
        # 同値も挙げてGrepする
        count_max = sum_count
        node_0_max = node_0
        node_1_max = node_1
        node_2_max = node_2

        s = '\nMax:' + '(' + node_0_max + ', ' + node_1_max + ', ' + node_2_max + ') : ' + 'Sum: ' + str(count_max) + '\n\n'
        f.write(s)
    else:
        s = '(' + node_0 + ', ' + node_1 + ', ' + node_2 + ') : ' + str(node_0) + ', ' + str(node_1) + ', ' + str(count_2) + ' length: ' + str(sum_count) + '\n\n'
        f.write(s)


print("★Result: ", node_0_max, node_1_max, node_2_max, count_max)
s = '\n★Result: ' + node_0_max + ' ' + node_1_max + ' ' + node_2_max + ' ' + 'Sum: ' + str(count_max) + '\n'
f.write(s)
f.close()

# ネットワークの可視化
nx.draw(G, with_labels = True, node_size = 200)
plt.show()
