"""
    author: wangyuxiang
    date: 2021-2-26

    数据预处理：
        从图文件中读取图数据，构建一个graph对象并返回
        其中图文件中数据格式为：
            96
            1 2 0.43753893752019957
            1 68 0.3533857046475604
            1 66 0.320978468597678
            ...

            其中第一行为结点个数，这里是96
            从第二行开始，以 src_node_id dst_node_id weight 的格式存储每一条边
            这里输入为有向图，即每一条边代表从源结点到目的结点的单向边；但这里简单起见，我们将其处理为无向图。
"""
from clusters.graph.graph import Graph
from clusters.graph.edge import Edge


class GetRealNetwork(object):

    def __init__(self, filename):
        self.filename = filename

    def get_graph(self):
        with open(self.filename, 'rb') as f:
            lines = f.readlines()
            vertices_number = int(lines[0])     # 第一行为结点个数
            graph = Graph(vertices_number)

            for line in lines[1:]:
                line = line.strip().split()
                src_id = int(line[0])
                dst_id = int(line[1])
                weight = float(line[2])
                graph.set_edges_number(graph.get_edges_number() + 2)

                '''
                    这里的处理有点难理解，因为输入是有向图，我们想要把他看作无向图处理，
                    因此对于一条边，我们为其创建两个edge对象：
                        - src_id -> dst_id
                        - dst_id -> src_id
                    并将其加入到对应的结点的邻居列表中。
                    
                    由于输入是有向图，那么有可能同一条边（两个方向）出现两次，此时我们只用添加一次就够。
                '''
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

        return graph


# 测试程序
if __name__ == '__main__':
    graph = GetRealNetwork('../data/Lymph6Graph').get_graph()
    print("Vertices number: ", graph.get_vertices_number())
    print("Edges number: ", graph.get_edges_number())
    print("Degree summary: ", graph.get_degree_sum())
    print("Degree of each node:")
    for i in range(1, 6):
        print("    Node %d's degree: %f" % (i, graph.get_vertice_degree_list()[i]))
    print("Neighbors of each node:")
    for i in range(1, 6):
        print("    Node %d's neighbor:" % i)
        for j in graph.get_vertice_connect_edge_list()[i]:
            print("        - %s" % j)
    print("Community number: ", graph.get_community_number())
