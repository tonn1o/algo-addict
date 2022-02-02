/**
 * @param {number} n - integer
 * @returns {string}
 */
function getNthNum(n) {
    let nthStr = '1';
    let i = 1;

    const getNthStr = (str) => {
        let res = '';
        let prev = null;
        let numCount = 0;

        for (let num of str) {
            if (prev && num !== prev) {
                res += numCount + prev;
                numCount = 0;
            }

            numCount += 1;
            prev = num;
        }

        return res + numCount + prev;
    }


    while (i < n) {
        nthStr = getNthStr(nthStr);
        i++;
    }

    return nthStr;
}
