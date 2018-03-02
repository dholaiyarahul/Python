import BianryTree

root=BianryTree.Node(7)
root.insert(9)
root.insert(2)
root.insert(5)
root.insert(8)
root.insert(1)
root.insert(4)
root.insert(15)
root.insert(12)
root.insert(16)

print(root.data)
print(root.leftchild.data)
print(root.rightchild.data)

#root.delete(5)

node,parent=root.lookup(4)
print(parent.data,'\n\n')

root.print_tree()