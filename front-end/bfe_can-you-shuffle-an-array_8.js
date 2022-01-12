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

const check = {};
const input = [1, 2, 3];

for (let i = 0; i < 100000; i++) {
    const res = shuffle(input).join('');
    check[res] = check[res] ? check[res] + 1 : 1;
}

console.log(check)
