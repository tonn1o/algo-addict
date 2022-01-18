function squareRoot(x) {
    let left = 0;
    let right = x / 2;

    while (left <= right) {
        const middle = Math.floor(left + (right - left) / 2);
        const middleSquare = middle * middle;

        if (middleSquare === x) {
            return middle;
        } else if (middleSquare > x) {
            right = middle - 1
        } else {
            left = middle + 1
        }
    }

    return x;
}
