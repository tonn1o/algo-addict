
/**
 * @param {Array<any>} promises - notice that input might contains non-promises
 * @return {Promise<Array<{status: 'fulfilled', value: any} | {status: 'rejected', reason: any}>>}
 */
function allSettled(promises) {
    if(!promises.length) {
        return Promise.resolve([]);
    }

    return new Promise((res) => {
        let settledCount = 0;
        const results = [];

        for (let i = 0; i < promises.length; i++) {
            Promise.resolve(promises[i]).then(
                value => results[i] = {status: 'fulfilled', value},
                reason => results[i] = {status: 'rejected', reason},
            ).finally(() => {
                settledCount++;

                if (settledCount === promises.length) {
                    res(results);
                }
            });
        }
    });
}

