import csv
import networkx as nx
import matplotlib.pyplot as plt
import itertools as itr

path = '/Users/keisu/Documents/GitHub/zone-energy/'
path_1 = '/Users/keisu/Documents/GitHub/zone-energy/50-500.txt'
path_2 = '/Users/keisu/Documents/GitHub/zone-energy/q3-sample.txt'
path_3 = '/Users/keisu/Documents/GitHub/zone-energy/5-94.txt'

# file open
with open(path_2) as f:
    reader = csv.reader(f, delimiter=' ')
    nodes_list = [row for row in reader]

print("nodes_list: ", nodes_list)
# nodes_list:  [['15', '23'], ['0', '3'], ['0', '4'], ... ['10', '12'], ['11', '14']]
# 15 nodes, 23 edges

print("nodes_list[1]: ", nodes_list[1])
# nodes_list[1]:  ['0', '3']

print("nodes_list[1][0]: ", nodes_list[1][0])
# nodes_list[1][0]:  0

# nodes list, start with nodes_list[1]
del nodes_list[0]
print("new nodes_list: ", nodes_list)

# Graphオブジェクトの作成
G = nx.Graph()

# まとめてnodeを追加
# G.add_nodes_from(["A", "B", "C", "D", "E", "F"])

# リストからまとめてnodeを追加
for node_pair in nodes_list:
    print("node_pair: ", node_pair)
    G.add_nodes_from(node_pair)

print("Nodes: ", G.nodes())

# まとめてedgeを追加
# G.add_edges_from([("A", "B"), ("B", "C"), ("B", "F"),("C", "D"), ("C", "E"), ("C", "F"), ("B", "F")])

# edgeを追加。有向グラフなので1つ目の引数がstart、2つ目の引数がtarget
for node_start, node_target in nodes_list:
    print("node_start: %s, node_target: %s" % (node_start, node_target))
    G.add_edge(node_start, node_target)

print("Edges: ", G.edges())

# G.remove_node(nodes_list[0][0])
# G.remove_node(nodes_list[0][1])

# Graphオブジェクトの情報
print("Info: ", nx.info(G))
# nodeの総数
print("number of nodes:", G.number_of_nodes())
# nodeの要素一覧
print("Nodes:", G.nodes())
# edgeの総数
print("Number of edges:", G.number_of_edges())
# edgeの要素一覧
print("Edges:", G.edges())
# 次数（nodeが持つedgeの数）
print("Degrees:", G.degree())

# 指定したノードに対する、隣接しているノードの数
print("Node: %s, Degree: %d" % ('0', G.degree('0')))
# 指定したノードに対する、隣接しているノードの一覧
print("nx.all_neighbors: ", list(nx.all_neighbors(G, '0')))

# ノードと隣接しているノードの数
for node in G.nodes():
    print("Node %s, Degree %d" % (node, G.degree(node)))

# 15C3 組み合わせ
nodes = G.nodes()
print("Sum of combinations: ", len(list(itr.combinations(nodes, 3))))

degree_max = 0
node_0 = ''
node_1 = ''
node_2 = ''

f = open(path + 'result.txt', 'w')
for x in itr.combinations(nodes, 3):
    print(x)
    node_0 = x[0]
    node_1 = x[1]
    node_2 = x[2]
    node_0_degree = len(list(nx.all_neighbors(G, node_0)))
    node_1_degree = len(list(nx.all_neighbors(G, node_1)))
    node_2_degree = len(list(nx.all_neighbors(G, node_2)))
    sum_of_degrees = node_0_degree + node_1_degree + node_2_degree

    s = '(' + node_0 + ', ' + node_1 + ', ' + node_2 + ') ' + str(node_0_degree) + ', ' + str(node_1_degree) + ', ' + str(node_2_degree) + ', ' + str(sum_of_degrees) + '\n'
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
        s = '(' + node_0_max + ', ' + node_1_max + ', ' + node_2_max + ') ' + str(node_0_degree) + ', ' + str(node_1_degree) + ', ' + str(node_2_degree) + ', ' + str(degree_max) + '\n'
        f.write(s)

f.close()
print(node_0_max, node_1_max, node_2_max, degree_max)

# ネットワークの可視化
nx.draw(G, with_labels = True, node_size = 200)
plt.show()
