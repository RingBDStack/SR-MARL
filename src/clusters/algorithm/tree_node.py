"""
    author: wangyuxiang
    date: 2021-2-27

    树节点类，包含：
        - 节点ID - int
        - 节点层级（高度） - int
        - 父节点 - TreeNode
        - 体积（该节点所划分的社区中所有图结点的度之和） - float
        - 父节点体积 - float
        - 割边数（该节点所划分的社区中连到社区外的边数） - float
        - 结构熵（每个节点都对应一个结构熵） - float
        - 孩子节点（是一个list，其中每个元素都为一个树节点对象） - [TreeNode]
        - 当前节点的所有子树的熵（是一个list，每个元素是对应子树的熵，也就是该子树所有节点熵之和） - [float]
        - 子树的最高层级（是一个list，每个元素是对应子树的最高层级（或者说高度）） - [int]
        - 叶子节点的原始社区（主要用于merge操作时判断原来社区和新的社区） - [string(node_id)]
        - 需要进行merge的新的社区 - [string(node_id)]
        - 当前节点的所有叶子节点（只有倒数第二层的节点会有这个值，其他层节点该值为空） - [string(node_id)]
        - 迭代次数（这个节点经过多少次迭代收敛） - int
        - MergeDetaHOfChildren（用来判断某两个社区merge后的熵之差，用来确定是否需要merge） - {TwoID: float}
        - CombineDetaHOfChildren（用来判断某两个社区combine后的熵之差，用来确定是否需要combine） - {TwoID: float}
"""


class TreeNode(object):

    def __init__(self, id, level, father, own_volumn, father_volumn, cut, structural_entropy_of_node,
                 children, entropy_of_childtree, highest_level_of_childtree, community_of_leaves1,
                 community_of_leaves2, all_leaves, iterate_number, merge_detaH_of_children,
                 combine_detaH_of_children):
        self.id = id
        self.level = level
        self.father = father
        self.own_volumn = own_volumn
        self.father_volumn = father_volumn
        self.cut = cut
        self.structural_entropy_of_node = structural_entropy_of_node
        self.children = children
        self.entropy_of_childtree = entropy_of_childtree
        self.highest_level_of_childtree = highest_level_of_childtree
        self.community_of_leaves1 = community_of_leaves1
        self.community_of_leaves2 = community_of_leaves2
        self.all_leaves = all_leaves
        self.iterate_number = iterate_number
        self.merge_detaH_of_children = merge_detaH_of_children
        self.combine_detaH_of_children = combine_detaH_of_children

    def __str__(self):
        return "TreeNode [ID=" + str(self.id) + ", Level=" + str(self.level) \
                        + ", OwnVolume=" + str(self.own_volumn) \
                        + ", FatherVolume=" + str(self.father_volumn) + ", Cut=" + str(self.cut) \
                        + ", StrutureEntropyOfNode=" + str(self.structural_entropy_of_node) \
                        + ", EntropyOfChildTree=" + str(self.entropy_of_childtree) \
                        + ", HightestLevelOfChildTree=" + str(self.highest_level_of_childtree) \
                        + ", CommunityOfLeaves1=" + str(self.community_of_leaves1) \
                        + ", CommunityOfLeaves2=" + str(self.community_of_leaves2) \
                        + ", AllLeaves=" + str(self.all_leaves) \
                        + ", IterateNumber=" + str(self.iterate_number) + "]"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_father(self):
        return self.father

    def set_father(self, father):
        self.father = father

    def get_own_volumn(self):
        return self.own_volumn

    def set_own_volumn(self, own_volumn):
        self.own_volumn = own_volumn

    def get_father_volumn(self):
        return self.father_volumn

    def set_father_volumn(self, father_volumn):
        self.father_volumn = father_volumn

    def get_cut(self):
        return self.cut

    def set_cut(self, cut):
        self.cut = cut

    def get_structural_entropy_of_node(self):
        return self.structural_entropy_of_node

    def set_structural_entropy_of_node(self, structural_entropy_of_node):
        self.structural_entropy_of_node = structural_entropy_of_node

    def get_children(self):
        return self.children

    def set_children(self, children):
        self.children = children

    def get_entropy_of_childtree(self):
        return self.entropy_of_childtree

    def set_entropy_of_childtree(self, entropy_of_childtree):
        self.entropy_of_childtree = entropy_of_childtree

    def get_highest_level_of_childtree(self):
        return self.highest_level_of_childtree

    def set_highest_level_of_childtree(self, highest_level_of_childtree):
        self.highest_level_of_childtree = highest_level_of_childtree

    def get_community_of_leaves1(self):
        return self.community_of_leaves1

    def set_community_of_leaves1(self, community_of_leaves1):
        self.community_of_leaves1 = community_of_leaves1

    def get_community_of_leaves2(self):
        return self.community_of_leaves2

    def set_community_of_leaves2(self, community_of_leaves2):
        self.community_of_leaves2 = community_of_leaves2

    def get_all_leaves(self):
        return self.all_leaves

    def set_all_leaves(self, all_leaves):
        self.all_leaves = all_leaves

    def get_iterate_number(self):
        return self.iterate_number

    def set_iterate_number(self, iterate_number):
        self.iterate_number = iterate_number

    def get_merge_detaH_of_children(self):
        return self.merge_detaH_of_children

    def set_merge_detaH_of_children(self, merge_detaH_of_children):
        self.merge_detaH_of_children = merge_detaH_of_children

    def get_combine_detaH_of_children(self):
        return self.combine_detaH_of_children

    def set_combine_detaH_of_children(self, combine_detaH_of_children):
        self.combine_detaH_of_children = combine_detaH_of_children
