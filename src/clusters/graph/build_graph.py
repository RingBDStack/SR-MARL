from clusters.graph.graph import Graph
from clusters.graph.edge import Edge
from numpy import sort
import copy
from clusters.algorithm.high_dimensional_structural_entropy_algorithm import HighDimensionalStructureEntropyAlgorithm


class BuildGraph(object):
    def __init__(self, cosine_similarity):
        self.cosine_similarity = cosine_similarity

    def build(self):
        scs = []
        graphs = []
        for k in range(self.cosine_similarity.shape[0]):
            cs = copy.deepcopy(self.cosine_similarity)
            for i in range(cs.shape[0]):
                node_neighbor = sort(copy.copy(cs[i, :]))
                index = node_neighbor[-1 * (k + 1)]
                for j in range(len(cs[i, :])):
                    if cs[i, j] < index:
                        cs[i, j] = 0.0
            for i in range(cs.shape[0]):
                for j in range(i + 1, cs.shape[0]):
                    if cs[i, j] != 0:
                        cs[j, i] = cs[i, j]
                    if cs[j, i] != 0:
                        cs[i, j] = cs[j, i]
            graph = Graph(cs.shape[0])
            for i in range(cs.shape[0]):
                for j in range(cs.shape[1]):
                    if i >= j or cs[i, j] == 0.0:
                        continue
                    src_id = i + 1
                    dst_id = j + 1
                    weight = cs[i, j]
                    edge1 = Edge(src_id, dst_id, weight)
                    edge2 = Edge(dst_id, src_id, weight)
                    bool_src = edge1 in graph.get_vertice_connect_edge_list()[src_id]
                    bool_dst = edge2 in graph.get_vertice_connect_edge_list()[dst_id]
                    graph.get_vertice_connect_edge_list()[src_id].add(edge1)
                    graph.get_vertice_connect_edge_list()[dst_id].add(edge2)

                    if not bool_src:
                        graph.get_vertice_degree_list()[src_id] += weight
                    if not bool_dst:
                        graph.get_vertice_degree_list()[dst_id] += weight
                    if not bool_src and not bool_dst:
                        graph.set_degree_sum(graph.get_degree_sum() + 2 * weight)
            algorithm = HighDimensionalStructureEntropyAlgorithm(graph)
            sc = algorithm.one_dimension()
            scs.append(sc)
            graphs.append(graph)
        index = len(scs) - 1
        for i in range(1, len(scs) - 1):
            if scs[i] < scs[i - 1] and scs[i] < scs[i + 1]:
                index = i
                break
        return graphs[index]
