/**
 * @param {HTMLElement} root
 * @param {HTMLElement} target
 * @return {HTMLElemnt | null}
 */
function nextRightSibling(root, target) {
    if (!root || !target) {
        return null;
    }

    const queue = [root, null];
    let right = null;

    while (queue.length) {
        const node = queue.shift();

        if (node === target) {
            return right;
        }

        right = node;

        if (!node) {
            queue.push(null);
            continue;
        }

        for (let i = node.children.length - 1; i >= 0; i--) {
            queue.push(node.children[i]);
        }
    }
}
