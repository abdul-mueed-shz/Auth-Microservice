import { LOGIN_INPUTS, SIGNUP_INPUTS } from "../reactive/reactives";

export function clearLoginInputs() {}
export function clearSignUpInputs() {
  for (let input in SIGNUP_INPUTS.value) {
    SIGNUP_INPUTS.value[input].v_model = null;
  }
}
