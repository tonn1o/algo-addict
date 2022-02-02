
/**
 * @param {string[][]} message
 * @return {string}
 */
function decode(message) {
    if (!message?.[0]?.length) {
        return '';
    }

    const maxRows = message.length;
    const maxCols = message[0].length;

    let row = 0;
    let col = 0;

    let direction = 'bottom';
    let result = '';

    while (col < maxCols) {
        const value = message[row][col];
        result += value;

        col++;

        if (direction === 'bottom' && row === maxRows - 1) {
            direction = 'top'
        } else if (direction === 'top' && row < 1) {
            direction = 'bottom'
        }

        if (direction === 'bottom') {
            row++;
        } else {
            row--;
        }
    }

    return result;
}
