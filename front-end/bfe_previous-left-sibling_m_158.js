/**
 * @param {Element} root
 * @param {Element} target
 * @return {Elemnt | null}
 */
function previousLeftSibling(root, target) {
  // your code here

  if (!root) {
    return null;
  }

  const queue = [root, null];
  let left = null;

  while (queue.length) {
    const node = queue.shift();

    if (node === target) {
      return left;
    }

    if (node === null) {
      left = null;
      queue.push(null);
      continue;
    }

    left = node;

    for (let child of node.children) {
      queue.push(child);
    }
  }

  return null;
}

