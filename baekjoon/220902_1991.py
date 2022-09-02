# 1991 트리 순회

N = int(input())

tree = {}
for i in range(N):
    o, l, r = input().split()
    tree[o] = [l, r]

pr = []
mi = []
po = []

# 전위 순회
def pre(A):
    pr.append(A)
    if tree[A][0] != '.':
        pre(tree[A][0])
    if tree[A][1] != '.':
        pre(tree[A][1])

# 중위 순회
def mid(A):
    if tree[A][0] != '.':
        mid(tree[A][0])
    mi.append(A)
    if tree[A][1] != '.':
        mid(tree[A][1])

# 후위 순회
def post(A):
    if tree[A][0] != '.':
        post(tree[A][0])
    if tree[A][1] != '.':
        post(tree[A][1])
    po.append(A)
    
    
pre('A')
mid('A')
post('A')

print(*pr, sep='')
print(*mi, sep='')
print(*po, sep='')