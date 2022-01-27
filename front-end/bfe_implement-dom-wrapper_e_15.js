function $(el) {
    return {
        css(property, value) {
            el.style[property] = value;
            return this;
        }
    }
}
