"""
    author: wangyuxiang
    date: 2021-2-26

    图模型类，包含：
        - 结点数
        - 边数
        - 所有结点度之和
        - 每一个结点的度，用一个list来表示，下标默认为结点ID
        - 每一个结点所连边的集合，用一个list来表示（下标默认为结点ID），
          其中每个元素是一个set，set的每个元素为Edge对象
        - CommunityOfEachVertice
        - VerticesOfEachCommunity
        - （划分）社区的数量
"""


class Graph(object):

    def __init__(self, vertices_number, edges_number=0, degree_sum=0.0, vertice_degree_list=None,
                 vertice_connect_edge_list=None, community_number=0):
        # 如果没有传入这些参数，那么修改其默认值
        if vertice_degree_list is None:
            vertice_degree_list = []
            for i in range(vertices_number + 1):
                vertice_degree_list.append(0)
        if vertice_connect_edge_list is None:
            vertice_connect_edge_list = []
            for i in range(vertices_number + 1):
                vertice_connect_edge_list.append(set())
        self.vertices_number = vertices_number
        self.edges_number = edges_number
        self.degree_sum = degree_sum
        self.vertice_degree_list = vertice_degree_list
        self.vertice_connect_edge_list = vertice_connect_edge_list  # [set(edge1,..), set(edge1,..), ... , set(edge1,..)]
        self.community_number = community_number

    def get_vertices_number(self):
        return self.vertices_number

    def set_vertices_number(self, vertices_number):
        self.vertices_number = vertices_number

    def get_edges_number(self):
        return self.edges_number

    def set_edges_number(self, edges_number):
        self.edges_number = edges_number

    def get_degree_sum(self):
        return self.degree_sum

    def set_degree_sum(self, degree_sum):
        self.degree_sum = degree_sum

    def get_vertice_degree_list(self):
        return self.vertice_degree_list

    def set_vertice_degree_list(self, vertice_degree_list):
        self.vertice_degree_list = vertice_degree_list

    def get_vertice_connect_edge_list(self):
        return self.vertice_connect_edge_list

    def set_vertice_connect_edge_list(self, vertice_connect_edge_list):
        self.vertice_connect_edge_list = vertice_connect_edge_list

    def get_community_number(self):
        return self.community_number

    def set_community_number(self, community_number):
        self.community_number = community_number
