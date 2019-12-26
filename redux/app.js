const intialState = { value: 0 };

const reducer = (action, previousState = {}) => {
    switch (action.type) {
        case "INCREMENT": return { value: previousState.value + 1 };
        case "DECREMENT": return { value: previousState.value - 1 };
    }
}

const store = createStore(reducer, intialState);

const callback = (newState) => {
    const { value: updatedValue } = newState;
    document.getElementById("counter").innerHTML = updatedValue;
}

store.subscribe(callback);

const increment = () => store.dispatch({ type: "INCREMENT" });
const decrement = () => store.dispatch({ type: "DECREMENT" });

document.getElementById("increment").addEventListener("click", increment);
document.getElementById("decrement").addEventListener("click", decrement);