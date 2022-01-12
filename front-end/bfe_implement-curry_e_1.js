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


function sum3(a, b, c){
    return a + b + c
};
const curried = curry(sum3);
