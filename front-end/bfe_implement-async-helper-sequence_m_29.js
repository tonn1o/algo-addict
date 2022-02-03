
/*
type Callback = (error: Error, data: any) => void

type AsyncFunc = (
   callback: Callback,
   data: any
) => void

*/

/**
 * @param {AsyncFunc[]} funcs
 * @return {(callback: Callback) => void}
 */
function sequence(funcs){
    const promisifiedFuncs = funcs.map(promisify);

    return function (callback, data) {
        let currentPromise = Promise.resolve(data)

        for (const promisified of promisifiedFuncs) {
            currentPromise = currentPromise.then(promisified);
        }

        currentPromise.then(res => callback(undefined, res)).catch(err => callback(err, undefined));
    }
}

function promisify(func) {
    return (...args) => new Promise((res, rej) => {
        func((error, data) => {
            if (error) {
                return rej(error);
            }
            res(data)
        }, ...args);
    })
};
