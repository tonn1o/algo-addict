function cloneDeep(data) {
    const visited = new Map();

    function clone(value) {
        if (typeof value !== "object" || value === null) {
            return value;
        }

        if (visited.has(value)) {
            return visited.get(value);
        }

        const result = Array.isArray(value) ? [] : {};

        visited.set(value, result);

        Reflect.ownKeys(value).forEach(key => {
            result[key] = clone(value[key]);
        })

        return result;
    }

    return clone(data);
}
