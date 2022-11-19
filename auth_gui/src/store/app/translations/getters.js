export function getMap(state) {
  return state.MAP;
}
export function getInput(state) {
  return (inputName) => {
    return MAP.INPUTS[inputName].V_MODEL;
  };
}
