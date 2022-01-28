
/**
 * @param {any} x
 * @return {number}
 */
function mySqrt(x) {
    if (isNaN(x) || typeof x !== 'number' || x < 0) {
        return NaN
    }

    if (x < 2) {
        return x;
    }

    let left = 2;
    let right = x / 2;

    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);
        const midSquare = mid * mid;

        if (midSquare === x) {
            return mid;
        } else if (midSquare > x) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return left - 1;
}

console.log(mySqrt(1))
