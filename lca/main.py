import collections
import itertools

# Human-readable tree structure
tree_schema = {
    1: {
        2: {
            4: {
                8: None,
                9: None
            },
            5: None
        },
        3: {
            6: None,
            7: None
        }
    }
}


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


def tree_from_schema(schema, parent=None):
    """Create tree structure from it's human-readable representation"""
    result = {}
    for k, v in schema.iteritems():
        current_node = Node(k, parent=parent)
        if isinstance(v, collections.Mapping):
            result.update({
                current_node: tree_from_schema(v, parent=current_node)
            })
        elif v is None:
            result.update({current_node: v})
    return result


def find_node(graph, value):
    """Find and return node object from graph"""
    for k, v in graph.iteritems():
        if k.value == value:
            return k
        elif isinstance(v, collections.Mapping):
            node = find_node(v, value)
            if node is not None:
                return node


def path_to_root(node):
    """Path from the node to the root of the tree"""
    # O(D) in wort case, where D is the graph depth
    result = [node.value]  # temporary list of length L
    current_node = node  # passed by reference, no object created
    while current_node.parent is not None:
        current_node = current_node.parent  # by ref, not copy
        result.append(current_node.value)
    return result


def lca(graph, value1, value2):
    """Lowest Common Ancestor for two nodes"""
    node_1 = find_node(graph, value1)
    node_2 = find_node(graph, value2)
    # Start measure complexity and memory
    path_1 = path_to_root(node_1)  # O(N)
    path_2 = path_to_root(node_2)  # O(M)
    # in python set intersection is O(1), but internally, in python core, it
    # is O(min(N, M)) where N, M is length of each set. O(M*N) in worst case.
    common_nodes = set(path_1) & set(path_2)  # length is D-1 in worst case
    # End measure complexity and memory.
    # Total O(2(log D)+M*N)
    # D - graph depth
    # M, N - found paths length
    # In worst case D = M = N, thus O(2(log D) + D**2)
    # So that with large D, we may use O(D**2)
    # Regarding memory consumption.
    # path_to_root require memory for list with size D in worst case.
    # So path_1 and path_2 may require memory for list of 2*D size.
    # common_nodes requires D-1 list in worst case.
    # So that we have to have memory to store 3*D - 1 list elements.
    for n in path_1:
        if n in common_nodes:
            return n


def main():
    graph = tree_from_schema(tree_schema)
    # print all available combinations
    for one, two in itertools.product(range(1, 10), repeat=2):
        print "lca(graph, {one}, {two}) = {result}".format(
            one=one, two=two, result=lca(graph, one, two)
        )

if __name__ == '__main__':
    main()
