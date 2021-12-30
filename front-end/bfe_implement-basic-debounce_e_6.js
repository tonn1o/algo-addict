/**
 * @param {Function} func
 * @param {number} wait
 */
function debounce(func, wait) {
    let timeout = null;

    return function(...args) {
        if (timeout) {
            clearTimeout(timeout);
        }

        timeout = setTimeout(() => func(...args), wait);
    }
}
