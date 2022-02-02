/**
 * @param {any[]} items
 * @param {number[]} newOrder
 * @return {void}
 */
function sort(items, newOrder) {
    for (let i = 0; i < items.length; i++) {
        while (i !== newOrder[i]) {
            const swapIdx = newOrder[i];
            swap(i, swapIdx, items);
            swap(i, swapIdx, newOrder);
        }
    }
}

function swap(i, j, arr) {
    let tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}
