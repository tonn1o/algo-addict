// copied from lib.es5.d.ts
declare interface Array<T> {
    myReduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T;
    myReduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T, initialValue: T): T;
    myReduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U
}

Array.prototype.myReduce = function (callback: any, initialValue?: any) {
    const hasInitialValue = arguments.length === 2;

    if (!hasInitialValue && !this.length) {
        throw new Error();
    }

    const initialIndex = hasInitialValue ? 0 : 1;
    let acc = hasInitialValue ? initialValue : this[0];

    for (let i = initialIndex; i < this.length; i++) {
        acc = callback(acc, this[i], i, this);
    }

    return acc;
}
