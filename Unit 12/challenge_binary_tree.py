class Node:
    def __init__(self, val):
        # Initialize the node with a value and set left and right children to None
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        # Initialize the binary tree with a root node
        self.root = Node(root)

def PrintTree(root):
    '''
    Function to print a binary tree in a structured format.
    '''
    # Define a helper function to calculate the height of the tree
    def height(root):
        # If the root is None (base case), return -1, else return 1 + max height of left and right subtrees
        return 1 + max(height(root.left), height(root.right)) if root else -1  
    
    # Calculate the number of levels (height) of the tree
    nlevels = height(root)
    # Calculate the width of the tree display based on the number of levels
    width =  pow(2, nlevels + 1)

    # Initialize a queue to store tuples containing node info (node, level, position, alignment)
    q = [(root, 0, width, 'c')]
    # Initialize a list to store each level's nodes and their positions
    levels = []

    # BFS loop to traverse the tree level by level
    while q:
        node, level, x, align = q.pop(0)  # Dequeue the first node from the queue
        
        if node:
            # If the current level is not in levels, add it as a new list
            if len(levels) <= level:
                levels.append([])

            # Append current node's info to its respective level
            levels[level].append([node, level, x, align])
            # Calculate the segment width to position children relative to the current node's position
            seg = width // (pow(2, level + 1))
            # Enqueue left child at the next level with updated position (aligned to the left)
            q.append((node.left, level + 1, x - seg, 'l'))
            # Enqueue right child at the next level with updated position (aligned to the right)
            q.append((node.right, level + 1, x + seg, 'r'))

    # For each level in the tree, format and print the node values and connecting lines
    for i, l in enumerate(levels):
        pre = 0         # Initialize previous position for nodes
        preline = 0     # Initialize previous position for lines
        linestr = ''    # String to store line connections (branches)
        pstr = ''       # String to store node values
        seg = width // (pow(2, i + 1))  # Calculate segment size for current level
        
        # Iterate through each node in the current level
        for n in l:
            valstr = str(n[0].val)  # Convert node value to string
            # For right-aligned nodes, add spacing and backslash with branch length
            if n[3] == 'r':
                linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                preline = n[2] 
            # For left-aligned nodes, add spacing and forward slash with branch length
            if n[3] == 'l':
                linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)  
                preline = n[2] + seg + seg // 2
            # Add spacing based on previous node position, then add the node value
            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr
            pre = n[2]
        # Print the line and node strings for the current level
        print(linestr)
        print(pstr)

# Example usage:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Print the tree
PrintTree(tree.root)
