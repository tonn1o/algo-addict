
/**
 * @param {HTMLElement | null} root
 * @return {HTMLElement[]}
 */
function flatten(root) {
    if(!root) {
        return [];
    }

    const queue = [root];
    const results = [];

    while (queue.length) {
        const node = queue.shift();

        results.push(node);

        for (const child of node.children) {
            queue.push(child);
        }
    }

    return results;
}
