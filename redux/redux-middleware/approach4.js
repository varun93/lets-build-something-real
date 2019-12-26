const store = createStore(reducer, {});
/*
    Hiding Monkey Patching
*/

// monkey patching for multiple functionalities
const logger = (store) => {
    const next = store.dispatch;
    return (action) => {
        console.log(store.getState());
        console.log(action);
        const result = next(action);
        console.log(nextState);
        return result;
    }
}

const crashReporter = (store) => {
    const next = store.dispatch;
    return (action) => {
        try {
            return next(action);
        } catch (error) {
            console.error('Caught an exception!', error);
            captureError(error);
        }
    }
}

// apply middlewares 
const applyMiddlewares = (store, middlewares) => {
    const middlewares = middlewares.slice();
    middlewares.reverse();
    middlewares.forEach(middleware => (store.dispatch = middleware(store)));
}

applyMiddlewares(store, [logger, crashReporter]);