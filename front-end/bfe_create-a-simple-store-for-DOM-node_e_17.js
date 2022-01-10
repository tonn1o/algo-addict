class NodeStore {
    data = {}

    /**
     * @param {Node} node
     * @param {any} value
     */
    set(node, value) {
        const key = node.__storeKey__ || Symbol();
        node.__storeKey__ = key;
        this.data[key] = value;
    }
    /**
     * @param {Node} node
     * @return {any}
     */
    get(node) {
        return this.has(node)
            ? this.data[node.__storeKey__]
            : undefined;
    }

    /**
     * @param {Node} node
     * @return {Boolean}
     */
    has(node) {
        return !!this.data.hasOwnProperty(node.__storeKey__)
    }
}
