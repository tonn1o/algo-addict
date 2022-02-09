
/**
 * @param {Function} func
 * @param {number} wait
 * @param {boolean} option.leading
 * @param {boolean} option.trailing
 */
function debounce(func, wait, option = {leading: false, trailing: true}) {
    let timerId = null;
    let lastCallArgs = null;
    const {leading, trailing} = option;

    return function debounced(...args) {
        if (!leading && !trailing) {
            return;
        }

        if (leading && !timerId) {
            func.apply(this, args);
        } else if (timerId || !leading) {
            lastCallArgs = args;
        }

        clearTimeout(timerId);

        timerId = setTimeout(() => {
            if (trailing && lastCallArgs) {
                func.apply(this, lastCallArgs);
            }

            timerId = null;
            lastCallArgs = null;
        }, wait);
    }
}
