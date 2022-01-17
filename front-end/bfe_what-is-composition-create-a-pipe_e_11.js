/**
 * @param {Array<(arg: any) => any>} funcs
 * @return {(arg: any) => any}
 */
function pipe(funcs) {
    return (arg) => funcs.reduce((acc, curr) => curr(acc), arg);
}
