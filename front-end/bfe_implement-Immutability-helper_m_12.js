/**
 * @param {any} data
 * @param {Object} command
 */
function update(data, command) {
    if (command.hasOwnProperty("$push")) {
        if (!Array.isArray(data)) {
            throw new Error("Data is not array");
        }

        return [...data, ...command["$push"]]
    }

    if (command.hasOwnProperty("$set")) {
        return command["$set"];
    }

    if (command.hasOwnProperty("$merge")) {
        if (!(typeof data === "object" && data !== null)) {a
            throw new Error("Data is not an object");
        }

        return {
            ...data,
            ...command["$merge"],
        }
    }

    if (command.hasOwnProperty("$apply")) {
        return command["$apply"](data);
    }

    const updateData = Array.isArray(data) ? [...data] : { ...data };

    for (const key in command) {
        updateData[key] = update(updateData[key], command[key]);
    }

    return updateData;
}
