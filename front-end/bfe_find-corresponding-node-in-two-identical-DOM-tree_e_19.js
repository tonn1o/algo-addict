
/**
 * @param {HTMLElement} rootA
 * @param {HTMLElement} rootB - rootA and rootB are clone of each other
 * @param {HTMLElement} nodeA
 */
const findCorrespondingNode = (rootA, rootB, target) => {
    function getPath() {
        const queue = [[rootA, []]];

        while (queue.length) {
            const [node, path] = queue.shift();

            if (node === target) {
                return path;
            }

            if (!node.childNodes?.length) {
                continue;
            }

            const children = node.childNodes;

            for (let i = 0; i < children.length; i++) {
                queue.push([children[i], [...path, i]])
            }
        }
    }

    function getNodeByPath(path) {
        let node = rootB;

        for (let index of path) {
            node = node.childNodes[index];
        }

        return node;
    }

    const path = getPath();
    return getNodeByPath(path);
}
