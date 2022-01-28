
/**
 * @param {Array<any>} promises - notice input might have non-Promises
 * @return {Promise<any[]>}
 */
function all(promises) {
    return new Promise(async (resolve, reject) => {
        const data = [];

        try {
            for (let promise of promises) {
                data.push(await promise);
            }

            resolve(data);
        } catch(e) {
            reject(e);
        }
    });
}


/**
 * @param {Array<any>} promises - notice input might have non-Promises
 * @return {Promise<any[]>}
 */
function all(promises) {
    return new Promise((resolve, reject) => {
        if (!promises.length) {
            resolve(promises);
        }

        const results = [];
        const isResolved = new Array(promises.length).fill(false);

        for (let i = 0; i < promises.length; i++) {
            const promise = promises[i];

            if (!promise.then) { // value not a promise
                results[i] = promise;
                isResolved[i] = true;

                if (!isResolved.includes(false)) {
                    resolve(results);
                }
                continue;
            }

            promise
                .then(res => {

                    isResolved[i] = true;
                    results[i] = res;

                    if (!isResolved.includes(false)) {
                        resolve(results);
                    }
                })
                .catch(err => reject(err));
        };
    });
}


// TEST
const printSomething1 = new Promise((res, rej) => setTimeout(() => res(1), 1000));
const printSomething2 = new Promise((res, rej) => setTimeout(() => res(2), 2000));
const printSomething3 = new Promise((res, rej) => setTimeout(() => res(3), 3000));

const results = all([1,
    2,
    Promise.resolve(1)
]).then(res => console.log(res)).catch(err => console.log(err))
