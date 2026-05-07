import os


INF = float('inf')

def create_gr(data_lines):
    gr = {}
    start_point = "START_NODE"
    end_point = "END_NODE"

    def insert_link(n1, n2, capacity):
        if n1 not in gr: 
            gr[n1] = {}
        if n2 not in gr: 
            gr[n2] = {}
            
        gr[n1][n2] = gr[n1].get(n2, 0) + capacity
        if n1 not in gr[n2]: 
            gr[n2][n1] = 0

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

    return gr, start_point, end_point


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
                
                if neighbor == target:
                    return True
                que.append(neighbor)
                
    return False


def get_max_cars(file_name):
    if not os.path.isfile(file_name):
        return 0

    with open(file_name, "r", encoding="utf-8") as file:
        content = file.readlines()
        
    valid_lines = [line.strip() for line in content if line.strip()]
    if len(valid_lines) < 3: 
        return 0

    gr, root, dest = create_gr(valid_lines)
    max_flow = 0
    while True:
        parent = {}

        if not find_path(gr, root, dest, parent):
            break

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

    return max_flow


if __name__ == "__main__":
    filepath = "roads.csv"
    res = get_max_cars(filepath)
    print(f"Макс к-сть машин: {res}")