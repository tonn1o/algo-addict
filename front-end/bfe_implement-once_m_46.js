/**
 * @param {Function} func
 * @return {Function}
 */
function once(func) {
    let result = null;
    let isCalled = false;

    return function(...args) {
        if(!isCalled) {
            isCalled = true;
            result = func.apply(this, args);
        }

        return result;
    }
}

