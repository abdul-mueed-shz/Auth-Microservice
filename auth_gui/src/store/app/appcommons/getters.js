export function getContext(state) {
  return state.context;
}

export function getAdminEmail(state) {
  return state.appConfig.administrationEmail || "mueed58200099@yahoo.com";
}

export function getAppConfig(state) {
  return state.appConfig;
}
