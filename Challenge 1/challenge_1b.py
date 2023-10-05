class Node:
    def __init__(self, label):
        self.label = label
        self.inbound_links = set()
        self.outbound_links = set()


class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = Node(label)

    def add_edge(self, from_label, to_label):
        self.add_node(from_label)
        self.add_node(to_label)
        self.nodes[from_label].outbound_links.add(to_label)
        self.nodes[to_label].inbound_links.add(from_label)


def identify_router(graph):
    max_connections = 0
    routers_with_max_connections = []

    for label, node in graph.nodes.items():
        total_connections = len(node.inbound_links) + len(node.outbound_links)

        if total_connections > max_connections:
            max_connections = total_connections
            routers_with_max_connections = [label]
        elif total_connections == max_connections:
            routers_with_max_connections.append(label)

    print(routers_with_max_connections)

    return routers_with_max_connections


def build_graph(graph_links: str):
    number_strings = graph_links.replace(" -> ", ",").split(",")

    number_list = [int(number_string) for number_string in number_strings]

    directed_graph = DirectedGraph()

    for index in range(1, len(number_list)):
        directed_graph.add_edge(number_list[index - 1], number_list[index])

    return directed_graph


# running Test cases
assert identify_router(build_graph("1 -> 2 -> 3 -> 5 -> 2 -> 1")) == [2]
assert identify_router(build_graph("1 -> 3 -> 5 -> 6 -> 4 -> 5 -> 2 -> 6 ")) == [5]
assert identify_router(build_graph("2 -> 4 -> 6 -> 2 -> 5 -> 6")) == [2, 6]


"""
The time complexity of the `identify_router` function is O(V), where V represents the number of nodes (routers) in the graph.
This complexity arises from iterating through all nodes once, counting their total connections (inbound and outbound links), 
and identifying routers with the highest number of connections. 

The additional operations per node are constant time and do not change the overall linear time complexity.
"""
