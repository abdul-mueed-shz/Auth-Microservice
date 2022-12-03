export function toggleContext({ commit }, val) {
  commit("toggleContext", val);
}

export function setAppSettings({ commit }, appInfo) {
  commit("setAppSettings", appInfo);
}
