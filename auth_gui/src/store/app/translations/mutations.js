export function setInput(state, input) {
  state.MAP.INPUTS[input.name].V_MODEL = input.value;
}
