import { boot } from "quasar/wrappers";

let globalStore;
export default boot(async ({ app, store }) => {
  // global Values
  app.config.globalProperties.$CRYPTO_CIPHER_KEY =
    process.env.CRYPTO_CIPHER_KEY;
  app.config.globalProperties.$CRYPTO_CIPHER_IV = process.env.CRYPTO_CIPHER_IV;
  app.config.globalProperties.$OTP_LENGTH = 6;
  //
  globalStore = store;
});

export function getGlobalStore() {
  return globalStore;
}
