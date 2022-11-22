from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances
from sklearn.preprocessing import MinMaxScaler
from clusters.algorithm.high_dimensional_structural_entropy_algorithm import HighDimensionalStructureEntropyAlgorithm
from clusters.graph.build_graph import BuildGraph
import numpy as np
from clusters.algorithm.priority_tree import compute_structural_entropy_of_node


def decode_two_dimension_tree(root, nodes_number):
    label = [0] * nodes_number
    for i, children in enumerate(root.get_children()):
        for node_id in children.get_all_leaves():
            label[int(node_id) - 1] = i
    return np.array(label), len(root.get_children())


def decode_three_dimension_tree(root, nodes_number):
    label = [0] * nodes_number
    index = 0
    for children_of_root in root.get_children():
        if children_of_root is not None:
            if children_of_root.get_iterate_number() == 0:
                print(1, len(children_of_root.get_all_leaves()))
                for node_id in children_of_root.get_all_leaves():
                    label[int(node_id) - 1] = index
                index += 1
            else:
                for children in children_of_root.get_children():
                    if children is not None:
                        print(2, len(children.get_all_leaves()))
                        for node_id in children.get_all_leaves():
                            label[int(node_id) - 1] = index
                        index += 1
    return np.array(label), index


def aggregate(node, action_repr, graph):
    if len(node.get_children()) == 0:
        return action_repr[int(node.get_all_leaves()[0]) - 1]
    else:
        repr_node = [0] * action_repr.shape[1]
        node_se = 0
        for children in node.get_children():
            node_se += compute_structural_entropy_of_node(children.get_cut(), 2 * graph.get_degree_sum(), children.get_own_volumn(), node.get_own_volumn())
        for children in node.get_children():
            se = compute_structural_entropy_of_node(children.get_cut(), 2 * graph.get_degree_sum(), children.get_own_volumn(), node.get_own_volumn())
            print(se, node_se)
            repr = aggregate(children, action_repr, graph)
            repr_node += (se / node_se) * repr
        return repr_node


def se_cluster(n_actions, action_repr):
    cf = 1 / (2 * n_actions)
    # Step 1: 相似度测量
    cs = np.corrcoef(action_repr)
    # cs = np.reshape(cosine_similarity(action_repr, action_repr), [-1, 1])
    # sc = MinMaxScaler()
    # cs = np.reshape(sc.fit_transform(cs), [n_actions, n_actions])
    # cs = np.reshape(pairwise_distances(action_repr, action_repr), [-1, 1])
    # sc = MinMaxScaler()
    # cs = 1. - np.reshape(sc.fit_transform(cs), [n_actions, n_actions])
    for i in range(n_actions):
        cs[i, i] = 0
    cf *= cs.mean()
    cs += cf
    # Step 2: 基于一维结构熵极小化原则构建k近邻图
    bg = BuildGraph(cs)
    graph = bg.build()
    # Step 3: 求解二维/三维最优编码树
    algorithm = HighDimensionalStructureEntropyAlgorithm(graph)
    two_dimension_tree = algorithm.two_dimension()
    # three_dimension_tree = algorithm.three_dimension()
    reprs = []
    for children in two_dimension_tree.get_root().get_children():
        reprs.append(aggregate(children, action_repr, graph))
    # Step 4: 聚类结果
    labels, n_clusters = decode_two_dimension_tree(two_dimension_tree.get_root(), n_actions)
    return labels, n_clusters, reprs
    # return decode_three_dimension_tree(three_dimension_tree.get_root(), n_actions)
