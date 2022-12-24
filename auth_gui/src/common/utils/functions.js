import { getGlobalStore } from "src/boot/globals";
import { INPUTS } from "../reactive/reactives";

const store = getGlobalStore();

export function resetInputs(inputType) {
  const currentAppName = store.getters["appcommons/getAppConfig"].app_name;
  INPUTS.value[currentAppName][inputType].forEach((input) => {
    input.v_model = null;
  });
}
