
/**
 * @param {object} obj
 * @param {string} methodName
 */
function spyOn(obj, methodName) {

    if (!obj.hasOwnProperty(methodName) || typeof obj[methodName] !== "function") {
        throw new Error(`${methodName} is not a function`);
    }

    const spiedFunc = obj[methodName];
    const calls = [];

    obj[methodName] = function(...args) {
        calls.push(args);
        return spiedFunc.apply(this, args);
    }

    return {
        calls
    }
}
