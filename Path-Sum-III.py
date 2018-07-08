

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

 
 def pathSum(self, root, sum):
    def traverse(root, val):
        if not root:
            return 0
        res = (val == root.val)
        res += traverse(root.left, val - root.val)
        res += traverse(root.right, val - root.val)
        return res
    if not root:
        return 0
    ans = traverse(root, sum)
    ans += self.pathSum(root.left, sum)
    ans += self.pathSum(root.right, sum)
    return ans

def pathSum(self, root, sum):
    d = collections.defaultdict(int)
    d[0] = 1
    def pSum(root, cur, sum):
        if not root: return 0
        res = 0
        cur += root.val
        if cur - sum in d:
            res += d[cur - sum]
        d[cur] += 1
        res += pSum(root.left, cur, sum) + pSum(root.right, cur, sum)
        d[cur] -= 1
        return res
    return pSum(root, 0, sum)