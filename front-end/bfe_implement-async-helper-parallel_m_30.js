
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
function parallel(funcs){
    // your code here
    return function(cb) {
        const results = [];
        let settledNum = 0;
        let isCompleted = false;

        for (let i = 0; i < funcs.length; i++) {
            funcs[i]((error, data) => {
                if(!isCompleted && error) {
                    isCompleted = true;
                    cb(error, undefined);
                } else if (!isCompleted) {
                    settledNum++;
                    results[i] = data;

                    if (settledNum === funcs.length) {
                        cb(undefined, results);
                    }
                }
            });
        }
    }
}
