/*
Given a matrix of characters that contains encoded message. The message for the matrix would be I R O C L E D.
Travers the matrix in zigzag way, to decode the message.
*/

const input = [
    ['I', 'B', 'C', 'A', 'L', 'K', 'A'],
    ['D', 'R', 'F', 'C', 'A', 'E', 'A'],
    ['G', 'H', 'O', 'E', 'L', 'A', 'D'],
];

function decode(input) {
    const maxRow = input.length - 1;
    const maxColumn = input[0].length - 1;
    const res = [];

    let direction = 'bottom';
    let col = 0;
    let row = 0;

    while (col <= maxColumn) {
        const cell = input[row][col];
        res.push(cell);

        col += 1;


        if (direction === 'bottom') {
            if (row < maxRow) {
                row += 1;
            } else {
                row -= 1;
                direction = 'top';
            }

            continue;
        }

        if (direction === 'top') {
            if (row > maxRow) {
                row -= 1;
            } else {
                row += 1;
                direction = 'bottom';
            }
        }
    }

    return res;
}

console.log(decode(input)); // [I R O C L E D];
