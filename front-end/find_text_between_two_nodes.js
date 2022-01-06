/*
Given two references to two DOM nodes, return the text between them.

Assume you have access to:
    * Node's children as an array: node.children
    * Node's parent: node.parentNode
    * Get text content of a node (naive approach): node.textContent
  
<html>
  <head>
  </head>
  <body>
    <main>
      <section>
        Text that shouldn't be in the output
        <div>Text that shouldn't be in the output</div>
        <header>
          Text that shouldn't be in the output
          <h1>Text that shouldn't be in the output</h1>
          <h2>On this Page</h2>  <!-- node1 -->
          <button>
            Jump to section
          </button>
        </header>
        <ul>
          <li><span><span><span><span><span><span>Properties</span></span></span></span></span></span></li>
          <li><span><span><span><span><span><span>Methods</span></span></span></span></span></span></li>
          <li><span><span><span><span><span><span>Examples</span></span></span></span></span></span></li>
          <li><span><span><span><span><span><span>Specifications</span></span></span></span></span></span></li>
          <li><span><span><span><span><span><span>Browser compatibility</span></span></span></span></span></span></li>
          <li><span><span><span><span><span><span>Related topics</span></span></span></span></span></span></li>
        </ul>
      </section>
    </main>
    <div>
      <article>
        text that should be included
        <p> <!-- node2 -->
          <span>
            The <strong>DOM</strong>&nbsp;<strong><code>Node</code></strong>&nbsp;interface is an abstract base class upon which many other DOM API objects are based, thus letting those object types to be used
            similarly and often interchangeably.
          </span>
          As an abstract class, there is no such thing as a plain <code>Node</code> object. All objects that implement <code>Node</code> functionality are based on one of its subclasses. Most notable are
          <strong><code>Document</code></strong>, <strong><code>Element</code></strong>, and <strong><code>DocumentFragment</code></strong>.
        </p>
        <p>
          Text that shouldn't be in the output
          In addition, every kind of DOM node is represented by an interface based on <code>Node</code>. These include <strong><code>Attr</code></strong>,
        </p>
      </article>
    </div>
  </body>
</html>  

The output should be:
["On this Page", "Jump to section", "Properties", "Methods", "Examples", "Specifications", "Browser compatibility", "Related topics", "text that should be included"]
*/

function getTextBetweenTwoNodes(node1, node2) {
    const res = []

    function dfs(node) {
        if (node == null) {
            return false
        }

        if(node === node2) {
            return true;
        }

        if (node.nodeType === 3) {
            const text = node.textContent.trim();

            if (text) {
                res.push(text)
            }
        }

        if (node.childNodes) {
            for (let child of node.childNodes) {
                if(dfs(child)) {
                    return true;
                }
            }
        }

        return false;
    }

    let currentNode = node1

    while (!dfs(currentNode)) {
        currentNode = currentNode.nextSibling || currentNode.parentNode.nextSibling;
    }

    return res;
}
