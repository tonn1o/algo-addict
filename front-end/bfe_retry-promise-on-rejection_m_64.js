
/**
 * @param {() => Promise<any>} fetcher
 * @param {number} maximumRetryCount
 * @return {Promise<any>}
 */
function fetchWithAutoRetry(fetcher, maximumRetryCount) {
    // your code here
    let count = maximumRetryCount;

    return new Promise((res, rej) => {
        const fetch = () => {
            return fetcher().catch(err => {
                if (count > 0) {
                    count--;
                    return fetch();
                } else {
                    rej(err)
                }
            })
        }

        fetch().then(result => res(result)).catch(err => rej(err));
    });
}
