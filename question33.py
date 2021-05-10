import csv
import networkx as nx
import matplotlib.pyplot as plt
import itertools as itr

path = '/Users/keisu/Documents/GitHub/zone-energy/'
path_1 = '/Users/keisu/Documents/GitHub/zone-energy/50-500.txt'
path_2 = '/Users/keisu/Documents/GitHub/zone-energy/q3-sample.txt'
path_3 = '/Users/keisu/Documents/GitHub/zone-energy/5-94.txt'

# data file open
with open(path_1) as f:
    reader = csv.reader(f, delimiter=' ')
    nodes_list = [row for row in reader]

# 結果ファイル保存
f = open(path + 'result.txt', 'w')

print("nodes_list: ", nodes_list)
# nodes_list:  [['15', '23'], ['0', '3'], ['0', '4'], ... ['10', '12'], ['11', '14']]
# 15 nodes, 23 edges
s = "nodes_list: " + str(nodes_list) + '\n'
f.write(s)

print("nodes_list[1]: ", nodes_list[1])
# nodes_list[1]:  ['0', '3']
s = "nodes_list[1]: " + str(nodes_list[1]) + '\n'
f.write(s)

print("nodes_list[1][0]: ", nodes_list[1][0])
# nodes_list[1][0]:  0
s = "nodes_list[1][0]: " + str(nodes_list[1][0]) + '\n'
f.write(s)

# nodes list, start with nodes_list[1]
del nodes_list[0]
print("new nodes_list: ", nodes_list)
s = "nodes_list: " + str(nodes_list) + '\n'
f.write(s)

# Graphオブジェクトの作成
G = nx.Graph()

# まとめてnodeを追加
# G.add_nodes_from(["A", "B", "C", "D", "E", "F"])

# リストからまとめてnodeを追加
for node_pair in nodes_list:
    print("node_pair: ", node_pair)
    s = "node_pair: " + str(node_pair) + '\n'
    f.write(s)
    G.add_nodes_from(node_pair)

print("Nodes: ", G.nodes())
s = "Nodes: " + str(G.nodes()) + '\n'
f.write(s)

# まとめてedgeを追加
# G.add_edges_from([("A", "B"), ("B", "C"), ("B", "F"),("C", "D"), ("C", "E"), ("C", "F"), ("B", "F")])

# edgeを追加。有向グラフなので1つ目の引数がstart、2つ目の引数がtarget
for node_start, node_target in nodes_list:
    print("node_start: %s, node_target: %s" % (node_start, node_target))
    s = "node_start: " + str(node_start) + ',' + "node_target: " + str(node_target) + '\n'
    f.write(s)
    G.add_edge(node_start, node_target)

print("Edges: ", G.edges())
s = "Edges: " + str(G.edges()) + '\n'
f.write(s)

# G.remove_node(nodes_list[0][0])
# G.remove_node(nodes_list[0][1])

# Graphオブジェクトの情報
print("Info: ", nx.info(G))
s = "Info: " + str(nx.info(G)) + '\n'
f.write(s)

# nodeの総数
print("G.number of nodes:", G.number_of_nodes())
s = "Info: " + str(nx.info(G)) + '\n'
f.write(s)

# nodeの要素一覧
print("G.nodes:", G.nodes())
s = "Info: " + str(nx.info(G)) + '\n'
f.write(s)

# edgeの総数
print("G.number of edges:", G.number_of_edges())
s = "G.number of edges: " + str(G.number_of_edges()) + '\n'
f.write(s)

# edgeの要素一覧
print("G.edges:", G.edges())
s = "G.edges: " + str(G.edges()) + '\n'
f.write(s)

# 次数（nodeが持つedgeの数）
print("G.degree:", G.degree())
s = "G.degree: " + str(G.degree()) + '\n'
f.write(s)

# 指定したノードに対する、隣接しているノードの数
print("Node: %s, Degree: %d" % ('0', G.degree('0')))
s = "Node: " + "'0' " + str(G.degree('0')) + '\n'
f.write(s)

# 指定したノードに対する、隣接しているノードの一覧
print("nx.all_neighbors: ", list(nx.all_neighbors(G, '0')))
s = "nx.all_neighbors: " + str(list(nx.all_neighbors(G, '0'))) + '\n'
f.write(s)

# ノードと隣接しているノードの数
for node in G.nodes():
    print("Node %s, Degree %d" % (node, G.degree(node)))
    s = "Node " + str(node) + ", Degree " + str(G.degree(node)) + '\n'
    f.write(s)

# 15C3 組み合わせ
nodes = G.nodes()
print("Sum of combinations: ", len(list(itr.combinations(nodes, 3))))
s = "Sum of combinations: " + str(len(list(itr.combinations(nodes, 3)))) + '\n'
f.write(s)

# 重複しないエッジの数を数える
number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
edges = G.edges()
print(edges)
# [('0', '3'), ('0', '4'), ..., ('11', '14')]
print(list(edges)[0])
# ('0', '3')

# 重複しないエッジの数のリスト作成
# 初期化
no_dupulicate = [['', 0] for i in range(number_of_nodes)]
# [['', 0], ['', 0], ['', 0], ..., ['', 0], ['', 0]]
# ノード代入
for n in range(0, number_of_nodes):
    no_dupulicate[n][0] = str(n)

print("No dupulicate: ", no_dupulicate)
# [['0', 0], ['1', 0], ['2', 0], ..., ['13', 0], ['14', 0]]

# 重複しないエッジの数をカウント
for i in range(0, number_of_edges):
    node_x, node_y = list(edges)[i]
    print("node_x: %s, node_y: %s" % (node_x, node_y))
    no_dupulicate[int(node_x)][1] += 1

print("No dupulicate: ", no_dupulicate)
# [['0', 3], ['1', 4], ['2', 4], ..., ['13', 0], ['14', 0]]
s = "No dupulicate: " + str(no_dupulicate) + '\n\n'
f.write(s)

# 15C3 組み合わせ総当たり
degree_max = 0
node_0 = ''
node_1 = ''
node_2 = ''

s = "---"
f.write(s)

# 15C3
for x in itr.combinations(nodes, 3):
    print(x)
    #('0', '3', '4')
    node_0, node_1, node_2 = x
    # node_0 = x[0]
    # node_1 = x[1]
    # node_2 = x[2]
    node_0_degree = no_dupulicate[int(node_0)][1]
    node_1_degree = no_dupulicate[int(node_1)][1]
    node_2_degree = no_dupulicate[int(node_2)][1]
    sum_of_degrees = node_0_degree + node_1_degree + node_2_degree

    s = '(' + node_0 + ', ' + node_1 + ', ' + node_2 + ') : ' + 'Edges: ' + str(node_0_degree) + ', ' + str(node_1_degree) + ', ' + str(node_2_degree) + ', ' + 'Sum: ' + str(sum_of_degrees) + '\n'
    f.write(s)

    print("Node[0] %s, Degree[0] %d" % (node_0, node_0_degree))
    print("Node[1] %s, Degree[1] %d" % (node_1, node_1_degree))
    print("Node[2] %s, Degree[2] %d" % (node_2, node_2_degree))
    print("Sum of Degrees: ", sum_of_degrees)
    if degree_max < sum_of_degrees:
        degree_max = sum_of_degrees
        node_0_max = node_0
        node_1_max = node_1
        node_2_max = node_2

        s = '\nMax:'
        f.write(s)
        s = '(' + node_0_max + ', ' + node_1_max + ', ' + node_2_max + ') : ' + 'Edges: ' + str(node_0_degree) + ', ' + str(node_1_degree) + ', ' + str(node_2_degree) + ', ' + 'Sum: ' + str(degree_max) + '\n'
        f.write(s)

print(node_0_max, node_1_max, node_2_max, degree_max)
s = 'Result: ' + node_0_max + ' ' + node_1_max + ' ' + node_2_max + ' ' + 'Sum: ' + str(degree_max) + '\n'
f.write(s)
f.close()

# ネットワークの可視化
nx.draw(G, with_labels = True, node_size = 200)
plt.show()
