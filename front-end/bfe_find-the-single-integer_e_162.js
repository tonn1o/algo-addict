// https://bigfrontend.dev/problem/find-the-single-integer

/**
 * @param {number[]} arr
 * @returns number
 */
function findSingle(arr) {
    const hasPairObj = {}

    arr.forEach(num => {
        if (hasPairObj.hasOwnProperty(num)) {
            hasPairObj[num] = true;
        } else {
            hasPairObj[num] = false;
        }
    })

    return +(Object.entries(hasPairObj).find(([, value]) => !value)[0])
}

const arr = [10, 2, 2 , 1, 0, 0, 10]
console.log(findSingle(arr))
