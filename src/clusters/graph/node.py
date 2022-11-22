"""
    author: wangyuxiang
    date: 2021-2-26

    图结点类，包含：
        - 结点ID
        - 结点度
        - 结点所在的（划分）社区ID
"""


class Node(object):

    def __init__(self, node_id, degree, community_id):
        self.node_id = node_id
        self.degree = degree
        self.community_id = community_id

    def __hash__(self):
        return hash(self.node_id)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if other.__dict__.get("node_id") == self.__dict__.get("node_id"):
                return True
        return False

    # Override 返回结点信息（字符串）
    def __str__(self):
        return str(self.node_id)

    def get_node_id(self):
        return self.node_id

    def set_node_id(self, node_id):
        self.node_id = node_id

    def get_degree(self):
        return self.degree

    def set_degree(self, degree):
        self.degree = degree

    def get_community_id(self):
        return self.community_id

    def set_community_id(self, community_id):
        self.community_id = community_id