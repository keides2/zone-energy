import csv
import networkx as nx
import matplotlib.pyplot as plt

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

# ネットワークの可視化
nx.draw(G, with_labels = True, node_size = 200)
plt.show()
