Function.prototype.mycall = function(thisArg, ...args) {
    const thisContext = Object(thisArg ?? window);
    const funcKey = Symbol();
    thisContext[funcKey] = this;
    const result = thisContext[funcKey](...args);
    delete thisContext[funcKey];
    return result;
}
