import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes with labels
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Add directed, weighted edges
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=2)
G.add_edge('C', 'B', weight=1)
G.add_edge('D', 'A', weight=4)

# Draw graph with edge weights
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=14, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Directed Weighted Graph")
plt.show()
