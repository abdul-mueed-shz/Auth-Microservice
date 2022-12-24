import { boot } from "quasar/wrappers";
import VueCryptojs from "vue-cryptojs";

export default boot(async ({ app }) => {
  app.use(VueCryptojs);
});
