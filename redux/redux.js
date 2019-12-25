const createStore = (reducer, initialState) => {
  const subscribers = [];
  let state = initialState;

  const getState = () => state;

  const dispatch = (action) => {
    state = reducer(action, state);
    subscribers.forEach(subscriber => subscriber(state));
  }

  // maybe push this?
  const subscribe = (subscriber) => subscribers.push(subscriber);
  return { dispatch, subscribe, getState };
}