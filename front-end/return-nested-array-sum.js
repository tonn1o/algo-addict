/*
* Return the sum of an array that contains either numbers or other arrays of numbers, and multiply the total of each array by its nested depth.
* */

const input = [1, 2, 3, [4, 5, 6, [7, 8, 9]]];
const expectedAnswer = 180;

function getNestedArraySum(nums, depth) {
    let sum = 0;
    
    for (let num of nums) {
        if (Array.isArray(num)) {
            sum += getNestedArraySum(num, depth + 1);
            continue;
        }
        
        sum += num;
    }
    
    return sum * depth;
}

const result = getNestedArraySum(input, 1) === expectedAnswer;
