/**
 * @param {HTMLElement} tree
 * @return {string[]}
 */
function getTags(tree) {
    const tags = new Set();

    const traverseTree = (node) => {
        tags.add(node.tagName.toLowerCase());

        if (node.children.length) {
            for (let child of node.children) {
                traverseTree(child)
            }
        }
    }

    traverseTree(tree);

    return Array.from(tags.values())
}

// TEST
const div = document.createElement('div')
const a = document.createElement('a')

div.append(a);
console.log(getTags(div));
