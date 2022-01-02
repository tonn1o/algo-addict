
/**
 * @param {any} data
 * @return {string}
 */

const ignoreTypes = new Set(["undefined", "symbol", "function"]);

function stringify(data) {
    if (typeof data !== "object" || data === null || Array.isArray(data) || data instanceof Date) {
        return stringifyValue(data);
    }

    return stringifyObject(data);
}

function stringifyObject(obj) {
    let stringifiedObj = "{";

    Object.entries(obj).forEach(([key, value]) => {
        if (ignoreTypes.has(typeof value)) {
            return;
        }

        stringifiedObj += `"${String(key)}":${stringifyValue(value)},`
    });

    const strLength = stringifiedObj.length;

    // get rid of the last comma
    if (stringifiedObj[strLength - 1] === ',') {
        stringifiedObj = stringifiedObj.slice(0, strLength - 1);
    }

    stringifiedObj += "}";

    return stringifiedObj;
}

function stringifyValue(value) {
    const type = typeof value;

    if (type === "bigint") {
        throw new Error();
    }

    if (ignoreTypes.has(type)) {
        if (type === "function") {
            return undefined;
        }

        return "null";
    }

    if (type === "boolean") {
        return value ? "true" : "false";
    }

    if (type === "string") {
        return `"${value}"`;
    }

    if (type === "number") {
        if (isNaN(value) || !isFinite(value)) {
            return "null"
        }
        return String(value);
    }

    if (value instanceof Date) {
        return `"${value.toISOString()}"`;
    }

    if (value === null) {
        return "null";
    }

    if (Array.isArray(value)) {
        const stringifiedValues = value.map(stringifyValue).join();
        return `[${stringifiedValues}]`;
    }

    if (type === "object") {
        return stringifyObject(value);
    }

    return String(value);
}


const testData = {
    id: 101,
    name: "Anton",
    isAdmin: true,
    contactData: {
        isInternationalPhone: true,
        phone: "+491111111",
        socialNetworks: ["facebook", "LinkedIn"]
    },
    friendsIds: [102, 103, 104, 105],
    isValid: null,
    phone: undefined,
    registrationDate: new Date(),
    articlesCount: Infinity,
    likes: NaN,
    symb: Symbol('key'),
    func: () => {}
}

console.log(JSON.stringify(testData) === stringify(testData));
