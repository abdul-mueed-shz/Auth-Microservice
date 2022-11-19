import { store } from "quasar/wrappers";
import { createStore } from "vuex";
import translation from "./app/translations";
import appcommons from "./app/appcommons";

export default store(function () {
  const Store = createStore({
    modules: {
      translation,
      appcommons,
    },

    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING,
  });

  return Store;
});
