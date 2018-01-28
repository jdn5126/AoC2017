# Recursive Circuits
import sys

class Node:
    def __init__(self, name, weight, children=None, parent=None):
        self.name = name
        self.weight = weight
        if children:
            self.children = children
        else:
            self.children = []
        self.parent = parent
        # Each node stores sum of sub_tree
        self.sub_sum = weight

    def append_child(self, child):
        self.children.append(child)

    def update_parent(self, parent):
        self.parent = parent

    def update_weight(self, weight):
        self.weight = weight

    def is_child(self, name):
        return name in self.children

    def is_leaf(self):
        return self.children is None


def get_root(tree):
    # Given any root, find parent
    node = tree.itervalues().next()
    while node.parent is not None:
        node = node.parent
    return node


def calc_sub_sums(node):
    # Store sums of all child nodes
    child_sums = {}
    badNode1 = None
    badNode2 = None
    for child in node.children:
        # Get sum of child subtree
        child_sum = calc_sub_sums(child)
        node.sub_sum += child_sum
        # check if this sum is good
        if child_sum in child_sums:
            child_sums[child_sum] += 1
        else:
            child_sums[child_sum] = 1
            if badNode1 is None:
                badNode1 = child
            else:
                badNode2 = child
    # bad nodes
    if badNode1 is not None and badNode2 is not None:
        if child_sums[badNode1.sub_sum] > 1:
            # badNode2 needs to change weight
            if badNode1.sub_sum > badNode2.sub_sum:
                # badNode2 needs to be increased
                print badNode2.weight + ( badNode1.sub_sum - badNode2.sub_sum )
            else:
                # badNode2 needs to be decreased
                print badNode2.weight - ( badNode2.sub_sum - badNode1.sub_sum )
        else:
            # badNode1 needs to change weight
            if badNode1.sub_sum > badNode2.sub_sum:
                # badNode1 needs to be decreased
                print badNode1.weight - ( badNode1.sub_sum - badNode2.sub_sum )
            else:
                # badNode1 needs to be increased
                print badNode1.weight + ( badNode2.sub_sum - badNode1.sub_sum )
        sys.exit()
    else:
        return node.sub_sum
        

def main(lines):
    tree = {}
    for line in lines:
        line = line.split("->")
        # Get node attributes
        node = line[0].split('(')
        name = node[0].strip()
        try:
            weight = int(node[1].replace(')', '').strip())
        except ValueError:
            print "Failure casting %s" % node[1]
            sys.exit()
        # Create or update Node
        try:
            my_node = tree[name]
            my_node.update_weight(weight)
            my_node.sub_sum = weight
        except KeyError:
            my_node = Node(name, weight)
            tree[name] = my_node
        # Handle children
        try:
            children_names = line[1].replace(',', '').split()
            # Create or update child
            for child_name in children_names:
                # Child exists
                try:
                    child_node = tree[child_name]
                    child_node.update_parent(my_node)
                except KeyError:
                    child_node = Node(child_name, weight=0, parent=my_node)
                    tree[child_name] = child_node
                my_node.append_child(child_node)
        except IndexError:
            continue

    # get root
    root = get_root(tree)
    # calculate sub_sums
    calc_sub_sums(root)


if __name__ == "__main__":
    f = open(sys.argv[1])
    main(f.readlines())
