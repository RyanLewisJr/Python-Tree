class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("The operation must be operated in subclass.")

        def __eq__(self, other):
            raise NotImplementedError("The operation must be operated in subclass.")

        def __ne__(self, other):
            return not(self == other)

    def root(self):
        raise NotImplementedError("The operation must be operated in subclass.")

    def parent(self):
        raise NotImplementedError("The operation must be operated in subclass.")

    def num_child(self):
        raise NotImplementedError("The operation must be operated in subclass.")

    def __len__(self):
        raise NotImplementedError("The operation must be operated in subclass.")

    def is_root(self, p):
        return self.root() is p

    def is_leaf(self, p):
        return self.num_child(p)

    def is_empty(self):
        return len(self) is 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1+self.depth(self.parent(p))

    def height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self.height2(c) for c in self.children(p))


class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError("The operation must be operated in subclass.")

    def right(self, p):
        raise NotImplementedError("The operation must be operated in subclass.")

    def sibling(self, p):
        parent = self.parent()
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class Node:
    __slots__ = '_element', '_parent', '_left', '_right'
    def __init__(self, element=None, parent=None, left=None, right=None):
        self._element = element
        self._parent = parent
        self._left = left
        self._right = right


class Position(BinaryTree.Position):
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def element(self):
        return self._node._element

    def __eq__(self, other):
        return type(other) is type(self) and self._node is other._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be self.Position.')
        if p._container is not self:
            raise ValueError('p must be self.')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self.root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists.')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left exists.')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(self._left)

    def _add_right(self, p, e):
        node = self.validate(p)
        if node._right is not None:
            raise ValueError('Right exists.')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replae(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Has 2 children.")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be leaf')
        if not type(self) is type(t1) is type(p2):
            raise TypeError('Tree types must be match.')
        self._size += len(t1)+len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
