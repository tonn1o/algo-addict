/**
 * @param { (...args: any[]) => any } fn
 * @returns { (...args: any[]) => any }
 */

function curry(fn) {
    const placeholder = curry.placeholder;

    return function curried(...args) {
        const sanitizedArgs = args.splice(0, fn.length);
        const hasPlaceholders = sanitizedArgs.includes(placeholder);

        if (!hasPlaceholders && sanitizedArgs.length >= fn.length) {
            return fn.apply(this, sanitizedArgs);
        }

        return function next(...newArgs) {
            const mergedArgs = [];

            sanitizedArgs.forEach(arg => {
                if (arg === placeholder && newArgs.length) {
                    mergedArgs.push(newArgs.shift());
                } else {
                    mergedArgs.push(arg);
                }
            });

            return curried.apply(this, [...mergedArgs, ...newArgs]);
        }
    }
}

curry.placeholder = Symbol()
