
/**
 * @param {any[]} arr
 */
function deduplicate(arr) {
    let length = arr.length;
    for (let i = 0; i < length; i++) {
        const value = arr[i];

        while(true) {
            const lastIndex = arr.lastIndexOf(value);

            if (lastIndex === i) {
                break;
            }

            arr.splice(lastIndex, 1);
            length--;
        }
    }

    return arr;
}
