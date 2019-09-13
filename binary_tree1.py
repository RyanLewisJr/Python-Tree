
class TNode:
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = TNode()

    def add(self, elem):
        node = TNode(elem)
        if not self.root:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()
                if cur_node.left is None:
                    cur_node.left = node
                elif cur_node.right is None:
                    cur_node.right = node
                else:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)

    def preorder(self, root):
        if root:
            print(root.elem)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        self.inorder(root.left)
        if root:
            print(root.elem)
        self.inorder(root.right)

    def postorder(self, root):
        self.postorder(root.left)
        self.postorder(root.right)
        if root:
            print(root.elem)

    def level_order(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            cur_node = queue.pop()
            print(cur_node.elem)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    def height(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            hl = self.height(root.left)
            hr = self.height(root.right)
            return max(hl, hr)+1

    def Nodes(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return self.Nodes(root.left)+self.Nodes(root.right)+1

    def Leaves(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return self.Leaves(root.left)+self.Leaves(root.right)

    def Non_Leaves(self, root):
        return self.Nodes(root)-self.Leaves(root)

    def Symmetry(self, root):
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False
        else:
            l = self.Symmetry(root.left)
            r = self.Symmetry(root.right)
            return l & r

    def reverse(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.reverse(root.left)
        self.reverse(root.right)

    def width(self, root):
        if not root:
            return 0
        queue = []
        queue.append(root)
        width = 0
        count = 0
        lastNode = root
        newLastNode = None
        while queue:
            cur_node = queue.pop()
            count += 1
            if cur_node.left:
                queue.append(cur_node.left)
                newLastNode = cur_node.left
            if cur_node.right:
                queue.append(cur_node.right)
                newLastNode = cur_node.right
            if cur_node is lastNode:
                lastNode = newLastNode
                if count > width:
                    width = count
                count = 0

    def Kth_Nodes(self, root, k):
        if k is 0 or not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return self.Kth_Nodes(root.left, k-1)+self.Kth_Nodes(root.right, k-1)

    def Haff_calc(self, root):
        if not root:
            return 0
        queue = []
        queue.append(root)
        h = 1
        total = 0
        lastNode = root
        newlastNode = None
        while queue:
            cur_node = queue.pop()
            total += h*cur_node
            if cur_node.left:
                queue.append(cur_node.left)
                newlastNode = cur_node.left
            if cur_node.right:
                queue.append(cur_node.right)
                newlastNode = cur_node.right
            if cur_node is lastNode:
                lastNode = newlastNode
                h += 1

    def Leaf(self, root):
        if not root:
            return
        elif not root.left and not root.right:
            print(root.elem)
        else:
            self.Leaf(root.left)
            self.Leaf(root.right)

    def same(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            hl = self.same(root1.left, root2.left)
            hr = self.same(root1.right, root2.right)
            return hl & hr


t = Tree()
for i in range(16):
    t.add(i)
t.preorder(t.root)
t.inorder(t.root)
t.postorder(t.root)
