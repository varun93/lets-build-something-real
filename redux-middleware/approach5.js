const store = createStore(reducer, {});
/*
    Removing Monkey Patching
*/

const logger = (store) => {
    return (next) => {
        return (action) => {
            console.log(store.getState());
            console.log(action);
            const result = next(action);
            console.log(nextState);
            return result;
        }
    }
}

const crashReporter = (store) => {
    return (next) => {
        return (action) => {
            try {
                return next(action);
            } catch (error) {
                console.error('Caught an exception!', error);
                captureError(error);
            }
        }
    }
}

// apply middlewares 
const applyMiddlewares = (store, middlewares) => {
    const middlewares = middlewares.slice();
    middlewares.reverse();
    let dispatch = store.dispatch;
    middlewares.forEach(middleware => (dispatch = middleware(store)(dispatch)));
    return Object.assign({}, store, { dispatch });
}

const newStore = applyMiddlewares(store, [logger, crashReporter]);