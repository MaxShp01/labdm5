import networkx as nx
import matplotlib.pyplot as plt

# створюємо перший граф
G1 = nx.DiGraph()
G1.add_nodes_from(range(8))
G1.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 5), (3, 6), (5, 6), (5, 7)])

# створюємо другий граф
G2 = nx.DiGraph()
G2.add_nodes_from(range(8))
G2.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 5), (3, 6), (5, 7), (6, 7)])

# візуалізація графів
plt.subplot(121)
nx.draw(G1, with_labels=True)
plt.title('Перший граф')
plt.subplot(122)
nx.draw(G2, with_labels=True)
plt.title('Другий граф')
plt.show()

# перевірка на ізоморфізм
if nx.is_isomorphic(G1, G2):
    print('Графи ізоморфні')
else:
    print('Графи неізоморфні')
