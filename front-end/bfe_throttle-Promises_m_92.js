
/**
 * @param {() => Promise<any>} func
 * @param {number} max
 * @return {Promise}
 */
function throttlePromises(fs, max){
    let funcs = fs;
    let results = [];

    return new Promise((resAll, rejAll) => {
        function makeAllRequests() {
            const requests = funcs.splice(0, max);

            Promise.all(requests.map(req => req())).then(res => {
                results = [...results, ...res];

                if(!funcs.length) {
                    resAll(results);
                } else {
                    makeAllRequests();
                }
            }).catch(err => {
                rejAll(err);
            })
        }

        return makeAllRequests();
    });
}

const apiCalls = [
    () => new Promise((res, rej) => setTimeout(() => {
        console.log('res: ', 1);
        res(1);
    }, 1000)),
    () => new Promise((res, rej) => setTimeout(() => {
        console.log('res: ', 2);
        res(2);
    }, 1000)),
    () => new Promise((res, rej) => setTimeout(() => {
        console.log('res: ', 3);
        res(3);
    }, 1000)),
    () => new Promise((res, rej) => setTimeout(() => {
        console.log('res: ', 4);
        res(4);
    }, 1000)),
    () => new Promise((res, rej) => setTimeout(() => {
        console.log('res: ', 5);
        res(5);
    }, 1000)),
    () => new Promise((res, rej) => setTimeout(() => {
        console.log('res: ', 6);
        res(6);
    }, 1000)),
];

throttlePromises(apiCalls, 2).then(res => {
    console.log(res);
}).catch(err => console.log(err));
