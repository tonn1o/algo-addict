"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[None]):
        self.val = val
        self.children = children
"""
import json

class Codec:

    def serialize(self, root: 'Node') -> str:
        if not root:
            return ''

        def dfs(node, currentLevel):
            currentLevel.append(node.val)

            if node.children is None:
                return currentLevel

            childrenNodes = []

            for child in node.children:
                dfs(child, childrenNodes)

            if childrenNodes:
                currentLevel.append(childrenNodes)

            return currentLevel


        return json.dumps(dfs(root, []))


    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None

        dataList = json.loads(data)

        if len(dataList) == 1:
            return Node(dataList[0], [])

        def dfs(node, children):
            prev = None
            childrenNodes = []

            for childVal in children:
                if isinstance(childVal, list):
                    dfs(prev, childVal)
                    continue

                cNode = Node(childVal, [])
                childrenNodes.append(cNode)
                prev = cNode

            if childrenNodes:
                node.children = childrenNodes

            return node


        return dfs(Node(dataList[0], []), dataList[1])


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
