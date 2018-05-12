import networkx as nx
import matplotlib.pyplot as plt 

G = nx.Graph()
G.add_node(179)
G.add_node(1, label = 'first node')
G.add_nodes_from([2, 3, 5])
G.add_edge(1, 5)
G.add_edges_from([(2,3), (5,3), (1,3), (179, 1)])

##nx.write_gexf(G, 'graph_file.gexf')
##G = nx.read_gexf('graph_file.gexf')

# для начала надо выбрать способ "укладки" графа. Их много, возьмём для начала такой:


##pos=nx.spring_layout(G)
##
##nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50) # рисуем узлы красным цветом, задаём размер узла
##nx.draw_networkx_edges(G, pos, edge_color='blue') # рисуем рёбра синим
##nx.draw_networkx_labels(G, pos, font_size=20, font_family='Arial') # добавим ещё подписи к узлам
##plt.axis('off') # по умолчанию график будет снабжён осями с координатами, здесь они бессмысленны, так что отключаем
##plt.show()


##G.add_edge(1, 3, weight=4) # вес ребра

##dg = nx.DiGraph()
##dg.add_weighted_edges_from([(1,4,0.5), (3,1,0.75)]) # от кого -- кому и вес ребра

print('nodes: ' + str(G.nodes()))
print('edges: ' + str(G.edges()))

# соседи узла 1
print('neigbours of node 1: ' + str(list(G.neighbors(1))))

# число соседей узла 5
print('degree of node 5: ' + str(G.degree(5)))

# Радиус графа, минимальный эксцентриситет среди всех вершин графа
print('radius: ' + str(nx.radius(G)))

# Диаметр графа, самый длинный путь от одной вершины до другой
print('diameter: ' + str(nx.diameter(G)))

# Плотность графа, отношение рёбер и узлов
print('density: ' + str(nx.density(G)))

# Коэффициент ассортативности (насколько сильно развалится если поубирать самые центральные узлы):
print('degree pearson correlation coefficient: ' + str(nx.degree_pearson_correlation_coefficient(G)))


# вот какой коэффициент у нашего графа
print('average clustering: ' + str(nx.average_clustering(G)))
print('transitivity: ' + str(nx.transitivity(G)))

# Центральность узлов (важность узлов)
deg = nx.degree_centrality(G)
print('degree centrality dict: ' + str(deg))
##for nodeid in sorted(deg, key=deg.get, reverse=True):
##    print(nodeid)
