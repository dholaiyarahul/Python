

class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    def getData(self):
        return self.data
    def insert(self,data):
        if self.data:
            if(self.data>data):
                if(self.leftchild==None):
                    self.leftchild=Node(data)
                else:
                    self.leftchild.insert(data)
            elif(self.data<data):
                if(self.rightchild==None):
                    self.rightchild=Node(data)
                else:
                    self.rightchild.insert(data)
        else:
            self.data=data
    def print_tree(self):
        if self.leftchild:
            self.leftchild.print_tree()
        print(self.data)
        if self.rightchild:
            self.rightchild.print_tree()
    def lookup(self,data,parent=None):
        if(self.data==data):
            return self,parent
        elif(data<self.data):
            if(self.leftchild==None):
                return None,None
            return self.leftchild.lookup(data,self)
        else:
            if(self.rightchild==None):
                return None,None
            return self.rightchild.lookup(data,self)
    def childrenCount(self):
        cnt=0
        if(self.leftchild):
            cnt+=1
        if(self.rightchild):
            cnt+=1
        return cnt
    '''
     def delete(self,data):
        if(self.childrenCount()==0):
            if parent:
                if(parent.leftchild) is node:
                    parent.leftchild=None
                else:
                    parent.rightchild=None
            else:
                self.data=None
        if(self.childrenCount()==1):
            if node.leftchild:
                n=node.leftchild
            else:
                n=node.rightchild
            if parent:
                if parent.leftchild is node:
                    parent.leftchild=n
                else:
                    parent.rightchild=n
                del node
            else:
                self.leftchild=n.leftchild
                self.rightchild=n.rightchild
                self.data=n.data
        else:

            # if node has 2 children

            # find its successor

            parent = node

            successor = node.right

            while successor.left:

            parent = successor
            successor = successor.left
# replace node data by its successor data

            node.data = successor.data
# fix successor's parent's child

            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right
    '''
root=Node(7)
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