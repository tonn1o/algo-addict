/**
 * @param {any} a
 * @param {any} b
 * @return {boolean}
 */
function isEqual(a, b) {
    const visited = new Map();

    function equal(a, b) {
        if (a === null || b === null, typeof a !== "object" || typeof b !== "object" ) {
            return a === b;
        }

        if (visited.has(a) && visited.has(b)) {
            return true;
        }

        visited.set(a, true);
        visited.set(b, true);

        const objectKeysA = Object.keys(a);
        const objectKeysB = Object.keys(b)

        if (objectKeysA.length !== objectKeysB.length) {
            return false;
        }

        for (const key of objectKeysA) {
            if(!equal(a[key], b[key])) {
                return false;
            }
        }

        return true;
    }

    return equal(a, b);
}
