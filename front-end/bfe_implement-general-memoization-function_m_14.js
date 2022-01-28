/**
 * @param {Function} func
 * @param {(args:[]) => string }  [resolver] - cache key generator
 */
function memo(func, resolver) {
    const cache = new Map();

    return function (...args) {
        const key = resolver ? resolver(...args) : Array.from(args).join('_');
        if(cache.has(key)) {
            return cache.get(key);
        } else {
            const result = func.call(this, ...args);
            cache.set(key, result);
            return result;
        }
    };
}

// TEST
const sum = (a, b) => {
    return a + b
}

const memoedSum = memo(sum, () => 'custom');

memoedSum(1, 2);
memoedSum(1, 2);
memoedSum(1, 3);
