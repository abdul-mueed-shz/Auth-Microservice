import { ref } from "vue";

export const INPUTS = ref({
  Starks: {
    LOGIN: [
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
    ],
    SINGUP: [
      {
        icon: "mdi-account",
        label: "FIRST_NAME",
        v_model: null,
      },
      {
        icon: "mdi-account-tie",
        label: "LAST_NAME",
        v_model: null,
      },
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
    ],
  },
  Licit: {
    LOGIN: [
      {
        icon: "mdi-mail",
        label: "EMAIL",
        v_model: null,
      },
    ],
    SINGUP: [
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
    ],
  },
});

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
    icon: "mdi-account",
    label: "FIRST_NAME",
    v_model: null,
  },
  {
    icon: "mdi-account-tie",
    label: "LAST_NAME",
    v_model: null,
  },
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
