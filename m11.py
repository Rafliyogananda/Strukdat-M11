class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class PohonAVL:
    def getTinggi(self, node):
        if not node:
            return 0
        return node.height

    def getKeseimbangan(self, node):
        if not node:
            return 0
        return self.getTinggi(node.left) - self.getTinggi(node.right)

    def rotasiKanan(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getTinggi(z.left), self.getTinggi(z.right))
        y.height = 1 + max(self.getTinggi(y.left), self.getTinggi(y.right))

        return y

    def rotasiKiri(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getTinggi(z.left), self.getTinggi(z.right))
        y.height = 1 + max(self.getTinggi(y.left), self.getTinggi(y.right))

        return y

    def sisipkan(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.sisipkan(root.left, key)
        else:
            root.right = self.sisipkan(root.right, key)

        root.height = 1 + max(self.getTinggi(root.left), self.getTinggi(root.right))

        keseimbangan = self.getKeseimbangan(root)

        if keseimbangan > 1:
            if key < root.left.key:
                return self.rotasiKanan(root)
            else:
                root.left = self.rotasiKiri(root.left)
                return self.rotasiKanan(root)

        if keseimbangan < -1:
            if key > root.right.key:
                return self.rotasiKiri(root)
            else:
                root.right = self.rotasiKanan(root.right)
                return self.rotasiKiri(root)

        return root

    def preOrder(self, root):
        if root:
            print("{0} ".format(root.key), end="")
            self.preOrder(root.left)
            self.preOrder(root.right)


pohonAVL = PohonAVL()
akar = None
kunci = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for k in kunci:
    akar = pohonAVL.sisipkan(akar, k)

print("Traversing preorder dari pohon AVL yang terkonstruksi adalah:")
pohonAVL.preOrder(akar)
