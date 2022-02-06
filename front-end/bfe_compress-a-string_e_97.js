
/**
 * @param {string} str
 * @return {string}
 */
function compress(str) {
    if (!str) {
        return '';
    }

    let result = '';
    let count = 0;

    for (let i = 0; i < str.length; i++) {
        count++;

        if (str[i] !== str[i + 1]) {
            result += `${str[i]}${count > 1 ? count : ''}`;
            count = 0;
        }
    }

    return result
}
