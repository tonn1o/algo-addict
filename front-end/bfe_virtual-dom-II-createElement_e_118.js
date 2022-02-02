/**
 * MyElement is the type your implementation supports
 *
 * type MyNode = MyElement | string
 */

/**
 * @param { string } type - valid HTML tag name
 * @param { object } [props] - properties.
 * @param { ...MyNode} [children] - elements as rest arguments
 * @return { MyElement }
 */
function createElement(type, props, ...children) {
    return {
        type,
        props,
        children,
    }
}


/**
 * @param { MyElement }
 * @returns { HTMLElement }
 */
function render(myElement) {
    if (typeof myElement === 'string') {
        return document.createTextNode(myElement);
    }

    const {type, props, children} = myElement;

    const element = document.createElement(type)

    for (const [propName, value] of Object.entries(props)) {
        element[propName] = value;
    }

    for (const child of children) {
        element.append(render(child));
    }

    return element;
}
