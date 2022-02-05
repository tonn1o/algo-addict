/**
 * @param {string} html
 * @param {string[]} keywords
 */
function highlightKeywords(html, keywords) {
    let result = '';

    function getEmEnd(start) {
        let hasEnd = false;
        let end = start; //4

        for (const keyword of keywords) { // "Hello"
            const length = keyword.length; // 5
            const potentialEnd = start + length;

            if(html.slice(start, potentialEnd) === keyword) { // 0, 4 = Hello
                hasEnd = true;
                end = Math.max(start + length, end);
            }
        }

        return hasEnd ? end : -1;
    }

    for (let i = 0; i < html.length; i++) {
        let emEnd = getEmEnd(i);

        if (emEnd !== -1) {
            while(true) {
                let nextEmEnd = getEmEnd(emEnd);

                if (nextEmEnd === -1) {
                    break;
                }

                emEnd = nextEmEnd;
            }

            result += `<em>${html.slice(i, emEnd)}</em>`
            i = emEnd - 1;
        } else {
            result += html[i];
        }
    }

    return result;
};
