/**
 * cancel all timer from window.setTimeout
 */

window.timeouts = new Set();
const originalSetTimeout = window.setTimeout;
const originalClearTimeout = window.clearTimeout;

function clearAllTimeout() {
    window.timeouts.forEach(timerId => {
        window.clearTimeout(timerId);
        window.timeouts.delete(timerId);
    });
}

window.setTimeout = (cb, time, ...args) => {
    const cbWrapper = () => {
        cb();
        window.timeouts.delete(timerId);
    }

    const timerId = originalSetTimeout(cbWrapper, time);
    window.timeouts.add(timerId);
    return timerId;
}

window.clearTimeout = (timerId) => {
    originalClearTimeout(timerId)
    window.timeouts.delete(timerId);
}
