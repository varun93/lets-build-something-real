const store = createStore(reducer, {});

/*
    Wrapping Dispatch
    Problems with the approach
*/
const dispatchAndLog = (action) => {
    console.log(store.getState());
    console.log(action);
    store.dispatch(action);
    console.log(store.getState());
}

// usage
dispatchAndLog(action);


