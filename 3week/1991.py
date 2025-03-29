n = int(input()) 
tree = {}


for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)


def pre(tree, ans, node):
    if node == ".":
        return
    ans.append(node)

    left = tree[node][0]
    pre(tree, ans, left)

    right = tree[node][1]
    pre(tree, ans, right)

def ins(tree, ans, node):
    if node == ".":
        return
    

    left = tree[node][0]
    ins(tree, ans, left)
    ans.append(node)    
    right = tree[node][1]
    ins(tree, ans, right)

def post(tree, ans, node):
    if node == ".":
        return

    left = tree[node][0]
    post(tree, ans, left)  
    right = tree[node][1]
    post(tree, ans, right)
    ans.append(node)  


ans = []
pre(tree, ans, "A")  
print("".join(ans))
ans = []
ins(tree, ans, "A")  
print("".join(ans))
ans = []
post(tree, ans, "A")  
print("".join(ans))
