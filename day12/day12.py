# Digital Plumber

import sys


graph = {}
groups = {}

def has_path(program_id, group):
    if program_id == group:
        return True
    # BFS
    visited = []
    queue = []
    queue.append(program_id)
    visited.append(program_id)
    while len(queue) > 0:
        # pop
        node = queue[-1]
        del queue[-1]
        for child in graph[node]:
            if child == group:
                return True
            if child in visited:
                continue
            else:
                visited.append(child)
                queue.append(child)
    return False


def build_graph(lines):
    for line in lines:
        line = line.strip().split(" <-> ")
        graph[line[0]] = [ x.strip() for x in line[1].split(',') ]

    # Figure out number of groups
    for program in graph.keys():
        # See if program has a path to an existing group, else create new group
        has_group = False
        for group in groups.keys():
            if has_path(program, group):
                has_group = True
                groups[group].append(program)
                break
        if not has_group:
            groups[program] = []
    return len(groups)


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    print build_graph(f.readlines())
