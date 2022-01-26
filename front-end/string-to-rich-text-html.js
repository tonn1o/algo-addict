/*
Given a string and a style array render HTML pretty much like a rich text editor.
For example: 'Hello, world', [[0, 2, 'i'], [4, 9, 'b'], [7, 10, 'u']]
Output: <i>Hel</i>l<b>o, <u>wor</u></b><u>l</u>d
*/

function renderText(string, styles = []) {
    const chars = string.split('');

    styles.forEach(([start, end, tag]) => {
        chars[start] = `<${tag}>`+ chars[start];
        chars[end] += `</${tag}>`;
    });

    const stringHtml = chars.join('');
    // DOMParser API helps to fix tags overlapping
    const validHtml = (new DOMParser()).parseFromString(stringHtml, 'text/html');
    document.body.innerHTML = validHtml.body.innerHTML;
}


renderText('Hello, world', [[0, 2, 'i'], [4, 9, 'b'], [7, 10, 'u']])
