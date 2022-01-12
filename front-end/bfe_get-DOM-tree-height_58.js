/**
 * @param {HTMLElement | null} tree
 * @return {number}
 */
function getHeight(tree) {
    let height = 0;

    if (!tree) {
        return 0;
    }

    const queue = [[tree, 1]];

    while (queue.length) {
        const [node, level] = queue.shift();
        height = Math.max(level, height);

        for (let child of node.children) {
            queue.push([child, level + 1]);
        }
    }

    return height;
}
