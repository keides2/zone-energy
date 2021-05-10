import csv
import networkx as nx
import matplotlib.pyplot as plt

path_1 = '/Users/keisu/Documents/GitHub/zone-energy/50-500.txt'
path_2 = '/Users/keisu/Documents/GitHub/zone-energy/q3-sample.txt'

# file open
with open(path_1) as f:
    reader = csv.reader(f, delimiter=' ')
    l = [row for row in reader]

print("l: ", l)
print("l[1]: ", l[1])
print("l[1][0]: ", l[1][0])

rg = l[0][0]

# Graphオブジェクトの作成
G = nx.Graph()
 
# nodeデータの追加
# G.add_nodes_from(["A", "B", "C", "D", "E", "F"])

for node in range(int(rg)):
        G.add_nodes_from(str(node))

# edgeデータの追加
# G.add_edges_from([("A", "B"), ("B", "C"), ("B", "F"),("C", "D"), ("C", "E"), ("C", "F"), ("B", "F")])
 
for node, edge in l:
    print(node, edge)
    G.add_edge(node, edge)

G.remove_node(l[0][0])
G.remove_node(l[0][1])

print(nx.info(G))
print("number of nodes:", G.number_of_nodes())
print("nodes:", G.nodes())
print("number of edges:", G.number_of_edges())
print("edges:", G.edges())
print("degrees:", G.degree())

for i in range(int(rg)):
    print("degrees of :", i, G.degree(str(i)), list(nx.all_neighbors(G, str(i))))

# ネットワークの可視化
nx.draw(G, with_labels = True, node_size = 200)
plt.show()
