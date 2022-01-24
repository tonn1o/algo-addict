// https://bigfrontend.dev/problem/find-the-single-integer

/*
* We have an array of integers, all integers appear twice except one integer.
* Write a function findUnique(arr), which return this unique integer.
* Input: [1, 1, 2, 2, 3, 3, 4]
* Output: 4
* */

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
