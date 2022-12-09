from enum import Enum


class FileType(Enum):
    DIRECTORY = 1
    FILE = 2


class Node():
    "Generic tree node."

    def __init__(self, name, type: FileType, children=None, data=None):
        self.name = name
        self.type = type
        self.children = []
        self.data = data if data is not None else 0

        self.parent = None

        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        if self.type == FileType.DIRECTORY:
            return f'{self.name} (DIR)'
        elif self.type == FileType.FILE:
            return f'{self.name} (FILE)'

    def add_child(self, node):
        assert isinstance(node, Node)
        node.parent = self
        self.children.append(node)


def construct_tree(lines: list):
    root = Node(name='/', type=FileType.DIRECTORY, children=[], data=0)

    current_node = root

    # there will be one or many cd, followed by one ls
    for line in lines:
        line = line.strip()
        if line.startswith('$ cd'):
            destination = line.split('cd')[1].strip()

            # start here
            if (destination == '/'):
                current_node = root
            elif (destination == '..'):
                # need to go back up to parent node and continue processing
                current_node = current_node.parent
            else:
                # make new node
                child_directory_name = f'{current_node.name}/{destination}'
                child_directory = Node(
                    name=child_directory_name, type=FileType.DIRECTORY)
                current_node.add_child(child_directory)
                current_node = child_directory

        elif (line.startswith('$ ls')):
            # we are adding to the current node
            pass

        # if not a command, must be directory or file!
        elif (line.startswith('dir')):
            # this is a directory
            pass

        # only other possible case is a file
        else:
            size, name = line.split(' ')
            size = int(size)

            current_node.add_child(
                Node(name=name, type=FileType.FILE, data=size))

    return root


def get_directory_size(node: Node):
    directory_size = 0

    for child in node.children:
        if child.type == FileType.DIRECTORY:
            directory_size += get_directory_size(child)
        elif child.type == FileType.FILE:
            directory_size += child.data

    return directory_size


def get_all_directory_sizes(root_node: Node, directory_sizes=None):
    if directory_sizes is None:
        directory_sizes = {}

    for child in root_node.children:
        if child.type == FileType.DIRECTORY:
            directory_size = get_directory_size(child)
            directory_sizes[child.name] = directory_size

            get_all_directory_sizes(child, directory_sizes=directory_sizes)

    return directory_sizes


with open('input/input.txt') as f:
    lines = f.readlines()

    # construct data structure
    root_node = construct_tree(lines)

    # traverse data structure and compute all directory sizes
    directory_sizes = get_all_directory_sizes(root_node)

    # get part two answer
    total_disk_space = 70_000_000
    required_unused_space = 30_000_000

    total_used_space = get_directory_size(root_node)
    current_unused_space = total_disk_space - total_used_space
    minimum_directory_to_delete_size = required_unused_space - current_unused_space

    smallest_directory_size = total_disk_space - required_unused_space
    for name, size in directory_sizes.items():
        if size <= smallest_directory_size and size >= minimum_directory_to_delete_size:
            smallest_directory_size = size

    print(smallest_directory_size)
