import { api } from "src/boot/axios";

export async function login({ commit }, payload) {
  try {
    const result = await api.post("login", payload);
    commit("setAuthDetails", {
      ...payload,
      auth_token: result.data.auth_token,
      refresh_token: result.data.refresh_token,
    });
    return result;
  } catch (err) {
    console.log(err.response.data.detail);
    return err.response;
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
    return err.response;
    // Create a showerror notification
  }
}
export async function verifyEmail({ commit }, payload) {
  try {
    const result = await api.post("send-otp", payload);
    return Promise.resolve(result);
  } catch (err) {
    console.log(err);
    return Promise.reject(err.response);
    // Create a showerror notification
  }
}
