/*
    Adding Logging Manually
    Problems   
*/
const store = createStore(reducer, {});
console.log(store.getState());
console.log(action);
store.dispatch(action);
console.log(store.getState());