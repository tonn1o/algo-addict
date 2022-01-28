Array.prototype.myMap = function(func, thisArg = this) {
    const length = this.length;
    const mappedArray = new Array(length);

    for (let i = 0; i < length; i++) {
        if (i in this) {
            mappedArray[i] = func.call(thisArg, this[i], i, this)
        }
    }

    return mappedArray;
}

// test
const arr = new Array(5)
arr[0] = 1
arr[2] = undefined
arr[4] = null

const res = arr.myMap((val, idx) => val);
