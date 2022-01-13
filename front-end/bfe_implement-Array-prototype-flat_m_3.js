
/**
 * @param { Array } arr
 * @param { number } depth
 * @returns { Array }
 */
function flat(arr, depth = 1) {
    const flatInner = (subArr, currentDepth = 1) => {
        const result = [];

        for (let item of subArr) {
            if (Array.isArray(item) && currentDepth <= depth) {
                result.push(...flatInner(item, currentDepth + 1));
                continue;
            }

            result.push(item);
        }

        return result
    };

    return flatInner(arr);
}
