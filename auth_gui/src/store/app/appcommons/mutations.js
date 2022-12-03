export function toggleContext(state, val) {
  if (val) {
    state.context = val;
    return;
  }
  state.context = !state.context;
}

export function setAppSettings(state, appInfo) {
  state.appConfig.app_name = appInfo.app_name;
  state.appConfig.redirect_url = appInfo.redirect_url;
}
