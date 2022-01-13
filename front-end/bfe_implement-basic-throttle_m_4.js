/**
 * @param {Function} func
 * @param {number} wait
 */

function throttle(func, wait) {
  let timeoutId = null;
  let lastArgs = null

  return (...args) => {
      if (timeoutId) {
        lastArgs = [...args]
        return; // do nothing if timeout is still there
      }

      func(...args);

      timeoutId = setTimeout(() => {
        timeoutId = null;

        if (lastArgs) {
          func(...lastArgs)
          lastArgs = null;
        }
      }, wait);
  }
}
