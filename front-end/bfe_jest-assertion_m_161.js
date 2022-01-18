function myExpect(input) {
  let reverse = false;

  return {
    toBe: (expected) => {
      const isExpected = reverse ? !Object.is(input, expected) : Object.is(input, expected);

      if (!isExpected) {
        throw Error();
      }
    },
    get not() {
      reverse = true;
      return this;
    }
  }
}



