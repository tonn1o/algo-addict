// ref: https://javascript.info/currying-partials

/**
 * @param { (...args: any[]) => any } fn
 * @returns { (...args: any[]) => any }
 */
function curry(fn) {
    return function internal(...args) {
        if (args.length >= fn.length) {
            return fn(...args);
        }

        return (...args2) => internal(...args.concat(args2));
    };
}

