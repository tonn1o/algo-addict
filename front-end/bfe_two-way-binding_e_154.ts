function model(state: {value: string}, element: HTMLInputElement) {
    element.value = state.value;

    Object.defineProperty(state, 'value', {
        set: (val: string) => { element.value = val },
        get: () => element.value,
    });
}
