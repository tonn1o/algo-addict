/**
 * @param {number} num
 */
function sum(num) {
    let base = num;

    function func(n) {
        base += n
        return func
    };

    func.valueOf = () => {
        return base;
    };
    return func;
}
