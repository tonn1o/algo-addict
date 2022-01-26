function virtualize(element) {
    if (element.nodeType === 3) { // Text node
        return element.textContent;
    } else if (element.nodeType !== 1) {
        return null;
    }

    const type = element.tagName.toLowerCase();
    const attributes = {};
    let children = [];

    for (let attr of element.attributes) {
        const attrName = attr.name === 'class' ? 'className' : attr.name;
        attributes[attrName] = attr.value;
    }

    for (let child of element.childNodes) {
        children.push(virtualize(child));
    }

    if (children.length === 1) {
        children = children[0]
    } else if (!children.length) {
        children = undefined;
    }

    return {
        type,
        props: {
            ...attributes,
            children,
        }
    }
}

function render(elem) {
    if (!(elem instanceof Object)) { // Text Node check
        return document.createTextNode(elem);
    }

    const domElement = document.createElement(elem.type);
    const children = elem.props.children;

    for (let attr in elem.props) {
        const attrValue = elem.props[attr];

        if (attr === 'className') {
            domElement.className = attrValue;
        } else if (attr !== 'children') {
            domElement.setAttribute(attr, attrValue);
        }
    }

    if(Array.isArray(children)) {
        for (let child of children) {
            domElement.append(render(child))
        }
    } else if (children) { // single child
        domElement.append(render(children))
    }

    return domElement;
}



// Test
const wrapper = document.createElement('div');
wrapper.setAttribute('className','wrapper');

const h1 = document.createElement('h1')
h1.setAttribute('className','title');
h1.innerText = 'Test';

const textNode = document.createTextNode('some text');

wrapper.append(h1)
wrapper.append(textNode)


const virtualizedTree = virtualize(wrapper);
const domTree = render(virtualizedTree);

console.log(virtualizedTree)
console.log(domTree.outerHTML)
