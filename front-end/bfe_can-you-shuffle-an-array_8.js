/**
 * @param {any[]} arr
 */
function shuffle(arr) {
    const array = [...arr];
    for (let i = 0; i < array.length; i++) {
        const j = (Math.floor(Math.random() * (i + 1)));
        const tmp = array[j];
        array[j] = array[i]
        array[i] = tmp;
    }

    return array;
}

// Probability test
const check = {};

for (let i = 0; i < 100000; i++) {
    const res = shuffle([1, 2, 3]).join('');
    check[res] = check[res] ? check[res] + 1 : 1;
}

console.log(check)
