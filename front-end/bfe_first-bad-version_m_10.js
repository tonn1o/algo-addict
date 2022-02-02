
/*
 type TypIsBad = (version: number) => boolean
 */

/**
 * @param {TypIsBad} isBad
 */
function firstBadVersion(isBad) {
    // firstBadVersion receive a check function isBad
    // and should return a closure which accepts a version number(integer)
    return (version) => {
        let left = 0;
        let right = version;

        while (left < right) {
            let mid = Math.floor(left + (right - left) / 2);

            if(isBad(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return isBad(left) ? left : -1;

        // write your code to return the first bad version
        // if none found, return -1
    }
}
