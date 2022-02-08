/**
 * @param {object} source
 * @param {string | string[]} path
 * @param {any} [defaultValue]
 * @return {any}
 */
function get(source, path, defaultValue = undefined) {
    if (typeof path !== "string" && !Array.isArray(path) || !path?.length) {
        return defaultValue;
    }

    const formattedPath = Array.isArray(path) ? path : formatPath(path);
    let data = source;

    while (formattedPath.length) {
        const key = formattedPath.shift();

        if (!data.hasOwnProperty(key)) {
            return defaultValue;
        }

        data = data[key];
    }

    return data;
}


function formatPath(path) {
    const result = [];
    const ignoredChars = new Set([".", "[", "]"]);

    for (const char of path) {
        if (ignoredChars.has(char)) {
            continue;
        }

        result.push(char);
    }

    return result;
}
