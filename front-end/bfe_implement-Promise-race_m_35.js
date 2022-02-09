/**
 * @param {Array<Promise>} promises
 * @return {Promise}
 */
function race(promises) {
    return new Promise((res, rej) => {
        let isSettled = false;

        for(const promise of promises) {
            promise.then(
                result => {
                    if (!isSettled) {
                        isSettled = true;
                        res(result);
                    };
                },
                error => {
                    if (!isSettled) {
                        isSettled = true;
                        rej(error)
                    };
                }
            );
        }
    });
}
