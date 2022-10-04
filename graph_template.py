import random


class Vertex:
    def __init__(self, value: str) -> None:
        # value is a word
        self.value = value

        # nodes that have an edge from this vertex
        self.adjacent: dict[Vertex, int] = {}

        self.neighbours: list[Vertex] = []
        self.neighbour_weights: list[int] = []

    def add_edge_to(self, vertex, weight=0) -> None:
        # adds edge to vertex we input, with weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex) -> None:
        # increments weight of edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        pass

    # initializes probability map
    def get_probability_map(self) -> None:
        for vertex, weight in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbour_weights.append(weight)

    def next_word(self):
        # randomly selects next word based on weights
        return random.choices(self.neighbours, weights=self.neighbour_weights)[0]


class Graph:
    def __init__(self) -> None:
        self.vertices: dict[str, Vertex] = {}

    def get_vertex_values(self) -> set[str]:
        # what are the values of all the vertices?
        # in other words, return all possible words
        return set(self.vertices.keys())

    def add_vertex(self, value: str) -> None:
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value: str) -> Vertex:
        # what if the value is not in the graph

        if value not in self.vertices:
            self.add_vertex(value)
            
        return self.vertices[value]

    def get_next_word(self, current_vertex: Vertex) -> Vertex:
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self) -> None:
        for vertex in self.vertices.values():
            vertex.get_probability_map()
