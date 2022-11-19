import { ref } from "vue";

export const LOGIN_INPUTS = ref([
  {
    icon: "mdi-mail",
    label: "EMAIL",
    v_model: null,
  },
  {
    icon: "mdi-lock",
    type: "password",
    label: "PASSWORD",
    v_model: null,
  },
]);

export const SIGNUP_INPUTS = ref([
  {
    icon: "mdi-mail",
    label: "EMAIL",
    v_model: null,
  },
  {
    icon: "mdi-lock",
    label: "PASSWORD",
    type: "password",
    v_model: null,
  },
]);
