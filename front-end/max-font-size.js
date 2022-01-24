/*
getMaxFontSize(textString, domNode). Return the maximum possible font-size that can be applied to the textString inside
domNode such that the textString will fit inside domNode without overflowing (i.e will be in a single line)
*/


/*
    Solution:

    The idea behind this solution is that font-size increases proportionally.
    So if we know text width with font-size 1px, we can easily calculate the rest.
    E.g. String "test" with font-size 1px has width 3px. If the same string would have text size 10px, the string width would be = 3px * 10px = 30px;
    maxFontSize = containerWidth / 1pxStringWidth
*/


function getMaxFontSize(textString, domNode) {
    const containerWidth = domNode.scrollWidth;
    const textElem = document.createElement('span');

    textElem.textContent = textString;
    textElem.style.visibility = 'hidden';
    textElem.style.position = 'absolute';
    textElem.style.fontSize = '1px';

    document.body.append(textElem);

    // getBoundingClientRect is used for a purpose of accuracy, since it return width with decimals
    const fontSizeMultiplier = textElem.getBoundingClientRect().width;

    textElem.remove();

    return Math.floor(containerWidth / fontSizeMultiplier)
}

const target = document.getElementById('target');

console.log(getMaxFontSize('Short string', target)); // 31
console.log(getMaxFontSize('Very long string with a lot of characters', target)); // 9

/*
    Test HTML:

    <style>
        .container {
            width: 150px;
            border: 3px solid black;
            overflow: visible;
            white-space: nowrap;
        }
    </style>

    <div id="target" class="container"></div>
*/
