/**
 * @param {string} input
 * @returns string
 */

function removeChars(input) { // abc
    const stack = []; // []

    for (let i = 0; i < input.length; i++) {
        const value = input[i]; // c

        if(value === "c" && stack[stack.length - 1] === "a") {
            stack.pop();
            continue;
        } else if (value !== "b") {
            stack.push(value);
        };
    }

    return stack.join('');
}


function removeChars(input) {
    let result = input; // a
    let didChange = false;


    while(true) {
        didChange = false;
        let str = '';  // a

        for (let i = 0; i < result.length; i++) {
            const char = result[i]; // a

            if(char === 'b') {
                didChange = true;
                continue;
            } else if (char === 'a' && result[i + 1] === 'c') {
                didChange = true;
                i++;
                continue;
            }

            str += char
        }

        result = str;

        if (!didChange) {
            return result;
        }
    }
}
