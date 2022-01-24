/*
* Write a function `flattenArr(arr)` that will flatten multidimensional array
*
* Input: [1, [2, 3], [[4]]]
* Output: [1, 2, 3, 4]
* */

function flattenArr(arr = []) {
    let res = []

    for (let elem of arr) {
        if (Array.isArray(elem)) {
            res = res.concat(flattenArr(elem));
            continue;
        }

        res.push(elem);
    }

    return res;
}

const testCases = [
    {input: [], expect: []},
    {input: [1, 2, 3], expect: [1, 2, 3]},
    {input: [[1]], expect: [1]},
    {input: [1, [2, 3], [[4]]], expect: [1, 2, 3, 4]},
    {input: [1, [2, 3], [[4]], [[[5]], [6], 7]], expect: [1, 2, 3, 4, 5, 6, 7]},
]

for (const testCase of testCases) {
    const res = flattenArr(testCase.input);
    const isValid = testCase.expect.every((item, i) => item === res[i]);

    if (!isValid) {
        throw new Error(`
          Input: ${testCase.input}\n
          Expected: ${JSON.stringify(testCase.expect)}\n 
          Actual Output: ${JSON.stringify(res)}
        `);
    }
}

console.log('Passed')
