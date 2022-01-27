const count = (() => {
    let currentCount = 0;

    const countInner = () => {
        currentCount += 1;
        return currentCount;
    }

    countInner.reset = () => currentCount = 0;

    return countInner;
})()
