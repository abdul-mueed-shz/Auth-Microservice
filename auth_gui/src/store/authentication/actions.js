import { api } from "src/boot/axios";

export async function login({ commit }, payload) {
  try {
    const result = await api.post("login", payload);
    commit("setAuthDetails", {
      ...payload,
      auth_token: result.data.auth_token,
    });
    return result;
  } catch (err) {
    console.log(err);
    // Create a showerror notification
  }
}
export async function signup({ commit }, payload) {
  try {
    const result = await api.post("register", payload);
    commit("setAuthDetails", payload);
    return result;
  } catch (err) {
    console.log(err);
    // Create a showerror notification
  }
}
