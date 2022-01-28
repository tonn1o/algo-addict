





/**
 * @param { (...args: any[]) => any } fn
 * @returns { (...args: any[]) => any }
 */
function curry(fn) {
    const placeholder = curry.placeholder;

    return (function inner(oldArgs, ...newArgs) {
        const combinedArgs = [...oldArgs];

        let skipPlaceholdersNum = 0;
        for (let newArg of newArgs.slice(0, fn.length)) {
            if (newArg === placeholder) {
                skipPlaceholdersNum += 1;
            } else {
                for (let i = 0; i < combinedArgs.length; i++ ) {
                    if (combinedArgs[i] === placeholder) {
                        if (skipPlaceholdersNum < 1) {
                            combinedArgs[i] = newArg;
                            break;
                        } else {
                            skipPlaceholdersNum -= 1;
                        }
                    }
                }
            }
        }

        if (combinedArgs.indexOf(placeholder) === -1) {
            return fn.apply(this, combinedArgs);
        } else {
            return inner.bind(this, combinedArgs);
        }
    })(Array(fn.length).fill(placeholder));
}


// TEST

curry.placeholder = Symbol()

const  join = (a, b, c) => {
    return `${a}_${b}_${c}`
}

const curriedJoin = curry(join)
const _ = curry.placeholder

curry(join)(_,_,3,4)(1,_)(2,5)
