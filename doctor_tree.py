class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent, name, direction=None):
        if self.root is None:
            self.root = DoctorNode(name)
            print(f"Root node '{name}' created.")
            return
        
        parent_node = self.find(parent)

        if parent_node is None:
            print(f"Parent node '{parent}' not found.")
            return

        if direction not in ("left", "right"):
            print("Direction must be 'left' or 'right'.")
            return
        
        if direction == "left":
            if parent_node.left is None:
                parent_node.left = DoctorNode(name)
                print(f"Inserted '{name}' to the left of '{parent}'.")
            else:
                print(f"Left child of '{parent}' already exists.")
        elif direction == "right":
            if parent_node.right is None:
                parent_node.right = DoctorNode(name)
                print(f"Inserted '{name}' to the right of '{parent}'.")
            else:
                print(f"Right child of '{parent}' already exists.")
                

    def _insert_recursive(self, node, name):
        if name < node.name:
            if node.left is None:
                node.left = DoctorNode(name)
            else:
                self._insert_recursive(node.left, name)
        else:
            if node.right is None:
                node.right = DoctorNode(name)
            else:
                self._insert_recursive(node.right, name)

    def find(self, name):
        return self._find_recursive(self.root, name)

    def _find_recursive(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find_recursive(node.left, name)
        if found:
            return found
        return self._find_recursive(node.right, name)
        
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.name)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.name)
            self._inorder_recursive(node.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.name)



# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
# replaced tree.root with insert method
tree.insert(None, "Dr. Croft")
tree.insert("Dr. Croft", "Dr. Phan", "left") 
tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")
tree.insert("Dr. NoParent", "Dr. Welp", "left")
tree.insert("Dr. Croft", "Dr. Oops", "baddirection")
tree.insert("Dr. Croft", "Dr. Overwrite", "left")

print("\nPreorder:", tree.preorder())
print("Inorder:", tree.inorder())
print("Postorder:", tree.postorder())