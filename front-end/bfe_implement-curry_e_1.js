/**
 * @param { (...args: any[]) => any } fn
 * @returns { (...args: any[]) => any }
 */
function curry(fn) {
    return function curryInner(...args) {
        if (args.length >= fn.length) {
            return fn.apply(this, [...args]);
        } else {
            return (...newArgs) => curryInner.apply(this, newArgs.concat(args));
        }
    }
}
