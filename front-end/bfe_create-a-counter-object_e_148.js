function createCounter() {
    let counter = 0;
    return {
        get count() {
            return counter++;
        }
    }
}

const counter = createCounter();
