export function toggleContext(state, val) {
  if (val) {
    state.context = val;
    return;
  }
  state.context = !state.context;
}
