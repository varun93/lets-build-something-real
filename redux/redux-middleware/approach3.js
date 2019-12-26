const store = createStore(reducer, {});
/*
    Monkey Patching
    Problems with the approach
    - Polluting the original implementation
    - Replace with any method you like, which doesn't honour the API 
*/
const next = store.dispatch;

store.dispatch = (action) => {
    console.log(store.getState());
    console.log(action);
    const result = next(action);
    console.log(store.getState());
    return result;
}

// monkey patching for multiple functionalities
const patchLogger = (store) => {
    const next = store.dispatch;
    store.dispatch = (action) => {
        console.log(store.getState());
        console.log(action);
        const result = next(action);
        console.log(nextState);
        return result;
    }
}

const patchError = (store) => {
    const next = store.dispatch;
    store.dispatch = (action) => {
        try {
            return next(action);
        } catch (error) {
            console.error('Caught an exception!', error);
            captureError(error);
        }
    }
}