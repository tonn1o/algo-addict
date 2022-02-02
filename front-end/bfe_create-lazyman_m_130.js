
// interface Laziness {
//   sleep: (time: number) => Laziness
//   sleepFirst: (time: number) => Laziness
//   eat: (food: string) => Laziness
// }

/**
 * @param {string} name
 * @param {(log: string) => void} logFn
 * @returns {Laziness}
 */
function LazyMan(name, logFn) {
    const queue = [sayHi];

    function sayHi(){
        logFn(`Hi, I'm ${name}.`);
    }

    function eat(food) {
        logFn(`Eat ${food}.`);
    }

    function sleep(sec) {
        return new Promise((res) => {
            setTimeout(() => {
                logFn(`Wake up after ${sec} second${sec > 1 ? 's' : ''}.`);
                res();
            }, sec * 1000);
        })
    }

    async function executeQueue() { // chain tasks execution
        for (const task of queue) {
            await task();
        }
    }

    setTimeout(() => {
        executeQueue();
    }, 0);

    return {
        eat: function(...args) {
            queue.push(() => eat(...args));
            return this;
        },
        sleep: function(...args) {
            queue.push(() => sleep(...args));
            return this;
        },
        sleepFirst: function(...args) {
            queue.unshift(() => sleep(...args));
            return this;
        },
    }
}
