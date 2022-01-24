/*
Write a function doesFit(textString, fontSize, domNode)`.
Return true/false based on if the textString can fit inside the domNode with given fontSize without overflowing.
 */


function doesFit(textString, fontSize, domNode) {
    // I assume that text can wrap within the domNode. And we should check that it fits both, vertically and horizontally
    const containerWidth = domNode.scrollWidth;
    const containerHeight = domNode.scrollHeight;

    const textElem = document.createElement('span');

    textElem.innerText = textString;
    textElem.style.fontSize = fontSize + 'px';
    textElem.style.visibility = 'hidden';
    textElem.style.position = 'absolute'; // prevent interupting element's flow

    domNode.prepend(textElem);

    // scrollHeight/Width for the inline element is always 0 in Chrome. For that reason I use offsetHeight/Width
    const isValid = textElem.offsetWidth <= containerWidth && textElem.offsetHeight <= containerHeight;

    textElem.remove();

    return isValid;
}

const node = document.getElementById('target');

console.log(doesFit('This text does fit', 22, node)); // true
console.log(doesFit('This text is too long, it doesn\'t fit', 40, node)); // false


/*
    Test HTML:

    <style>
        .container {
            font-size: 16px;
            margin-top: 40px;
            width: 150px;
            border: 3px solid black;
            overflow: visible;
            white-space: nowrap;
            height: 50px;
        }
    </style>

    <div id="target" class="container"></div>
*/
