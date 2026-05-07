import os
import networkx as nx
import matplotlib.pyplot as plt

INF = float('inf')

def create_gr(data_lines):
    gr = {}
    start_point = "START_NODE"
    end_point = "END_NODE"

    def insert_link(n1, n2, capacity):
        if n1 not in gr: gr[n1] = {}
        if n2 not in gr: gr[n2] = {}
        gr[n1][n2] = gr[n1].get(n2, 0) + capacity
        if n1 not in gr[n2]: gr[n2][n1] = 0

    farm_list = [f.strip() for f in data_lines[0].split(",")]
    for farm in farm_list:
        insert_link(start_point, farm, INF)

    store_list = [s.strip() for s in data_lines[1].split(",")]
    for store in store_list:
        insert_link(store, end_point, INF)

    for row in data_lines[2:]:
        elements = row.split(",")
        if len(elements) == 3:
            insert_link(elements[0].strip(), elements[1].strip(), int(elements[2].strip()))

    return gr, start_point, end_point, farm_list, store_list

def find_path(gr, start, target, route):
    vis = {start}
    que = [start]
    head = 0
    while head < len(que):
        current_node = que[head]
        head += 1
        for neighbor, cap in gr[current_node].items():
            if cap > 0 and neighbor not in vis:
                route[neighbor] = current_node
                vis.add(neighbor)
                if neighbor == target: return True
                que.append(neighbor)
    return False

def visualize_max_flow(filename):
    if not os.path.isfile(filename):
        print(f"Помилка: Файл {filename} не знайдено!")
        return

    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()
        
    valid_lines = [line.strip() for line in content if line.strip()]
    if len(valid_lines) < 3: return

    gr, root, dest, farms, stores = create_gr(valid_lines)
    
    original_capacities = {}
    for row in valid_lines[2:]:
        elements = row.split(",")
        if len(elements) == 3:
            u, v, cap = elements[0].strip(), elements[1].strip(), int(elements[2].strip())
            original_capacities[(u, v)] = cap

    max_flow = 0
    while True:
        parent = {}
        if not find_path(gr, root, dest, parent): break
        path_flow = INF
        node = dest
        while node != root:
            prev_node = parent[node]
            path_flow = min(path_flow, gr[prev_node][node])
            node = prev_node
        max_flow += path_flow
        node = dest
        while node != root:
            prev_node = parent[node]
            gr[prev_node][node] -= path_flow
            gr[node][prev_node] += path_flow
            node = prev_node

    print(f"Розрахунок завершено. Максимальна кількість машин: {max_flow}")
    print("Малюємо вікно з графом...")

    G = nx.DiGraph()
    
    for f in farms: G.add_node(f, layer=0)
    for s in stores: G.add_node(s, layer=2)
        
    for (u, v), cap in original_capacities.items():
        if u not in G.nodes: G.add_node(u, layer=1)
        if v not in G.nodes: G.add_node(v, layer=1)
        
        flow = gr[v][u] 
        G.add_edge(u, v, capacity=cap, flow=flow)

    plt.figure(figsize=(12, 8))
    plt.title(f"Логістика компанії 'Квітка' (Всього доставлено: {max_flow} машин)", fontsize=16, fontweight='bold')

    pos = nx.multipartite_layout(G, subset_key="layer", align="horizontal")

    node_colors = []
    for node in G.nodes():
        if node in farms: node_colors.append('lightgreen')
        elif node in stores: node_colors.append('lightblue')
        else: node_colors.append('lightgray')

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500, edgecolors='black', linewidths=1.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    edges = G.edges(data=True)
    
    bottleneck_edges = [(u, v) for u, v, d in edges if d['flow'] == d['capacity'] and d['capacity'] > 0]
    flow_edges = [(u, v) for u, v, d in edges if 0 < d['flow'] < d['capacity']]
    unused_edges = [(u, v) for u, v, d in edges if d['flow'] == 0]

    nx.draw_networkx_edges(G, pos, edgelist=unused_edges, edge_color='lightgray', style='dashed', arrows=True, arrowsize=15)
    nx.draw_networkx_edges(G, pos, edgelist=flow_edges, edge_color='royalblue', width=2.5, arrows=True, arrowsize=20)
    nx.draw_networkx_edges(G, pos, edgelist=bottleneck_edges, edge_color='crimson', width=4.0, arrows=True, arrowsize=20)

    edge_labels = {(u, v): f"{d['flow']}/{d['capacity']}" for u, v, d in edges}
    
    bottleneck_labels = {k: v for k, v in edge_labels.items() if k in bottleneck_edges}
    other_labels = {k: v for k, v in edge_labels.items() if k not in bottleneck_edges}

    nx.draw_networkx_edge_labels(G, pos, edge_labels=other_labels, font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=bottleneck_labels, font_size=12, font_color='red', font_weight='bold')

    info_text = (
        "Інфа:\n"
        "• Зелені - Квіткові Ферми\n"
        "• Сині - Магазини\n"
        "• Сірі пунктирні дороги - Не використовуються\n"
        "• Товсті сині дороги - Їдуть машини\n"
        "• Червоні дороги - Забиті на 100% (Вузьке горлечко)"
    )
    plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes, 
             fontsize=10, fontweight='bold', verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='white', edgecolor='black', alpha=0.9))

    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    filepath = 'roads.csv'
    visualize_max_flow(filepath)