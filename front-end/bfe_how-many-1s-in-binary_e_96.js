
/**
 * @param {number} num - integer
 * @return {number} count of 1 bit
 */
function countOne(num) {
    let res = 0
    const str = (num >>> 0).toString(2)

    for (let char of str) {
        if (char === "1") {
            res += 1
        }
    }

    return res
}
