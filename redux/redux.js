const createStore = (reducer, initialState) => {
  const subscribers = [];
  let state = initialState;

  const getState = () => state;

  const dispatch = (action) => {
    state = reducer(action, state);
    subscribers.forEach(subscriber => subscriber(state));
    return action;
  }

  const subscribe = (subscriber) => subscribers.push(subscriber);

  const unsubscribe = (subscriber) => {
    const index = subscribers.indexOf(subscriber);
    subscribers.splice(index, 1);
  };

  return { dispatch, subscribe, unsubscribe, getState };
}