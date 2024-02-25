class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data, node):
        if node == None:
            # print(f"inserting {data}")
            return Node(data)
        if data > node.data:
            # print(f"inserting to right of {node.data} : {data}")
            if node.right == None:
                node.right  = self.insert(data, node.right)
            else:
                self.insert(data, node.right)
        elif data < node.data:
            # print(f"inserting to the left of {node.data} : {data}")
            if node.left == None:
                node.left = self.insert(data, node.left)
            else:
                self.insert(data, node.left)

  
    def InOrderTraversal(self, root):
        res = []
        if root :
            self.InOrderTraversal(root.left)
            print(root.data, end=" ")
            self.InOrderTraversal(root.right)
        
    def levelOrderTraversal(self, root):
        q = []
        q.append(root)
        print("\n")
        while ( len(q) > 0):
            print(q[0].data, end=" ")
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        

    def leftView(self, root):
        q = []
        q.append(root)
        # print("\n")
        while ( len(q) > 0):
            n = len(q)
            for i in range(1, n+1):
                node = q.pop(0)
                if i == 1:
                    print(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            

root = Node(27)
root.insert(14, root)
root.insert(35, root)
root.insert(10, root)
root.insert(19, root)
root.insert(31, root)
root.insert(42, root)
print("In order Traversal....")
root.InOrderTraversal(root)
print("\n\nLeft View...")
root.leftView(root)


