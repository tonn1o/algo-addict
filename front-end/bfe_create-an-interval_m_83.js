const timersMap = new Map();

/**
 * @param {Function} func
 * @param {number} delay
 * @param {number} period
 * @return {number}
 */
function mySetInterval(func, delay, period) {
    const timerIdKey = Symbol();

    const timer = (callCount = 0) => {
        const time = delay + period * callCount;
        const timerId = setTimeout(() => {
            func();
            timer(callCount + 1);
        }, time);

        timersMap.set(timerIdKey, timerId)
    }

    timer();
    return timerIdKey;
}

/**
 * @param { number } id
 */
function myClearInterval(id) {
    clearTimeout(timersMap.get(id));
}
