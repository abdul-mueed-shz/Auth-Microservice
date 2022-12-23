import { ref } from "vue";

export const INPUTS = ref({
  Starks: {
    LOGIN: [
      {
        icon: "mdi-mail",
        label: "EMAIL",
        v_model: null,
        min_length: 6,
      },
      {
        icon: "mdi-lock",
        type: "password",
        label: "PASSWORD",
        v_model: null,
        min_length: 7,
      },
    ],
    SINGUP: [
      {
        icon: "mdi-account",
        label: "FIRST_NAME",
        v_model: null,
        min_length: 2,
      },
      {
        icon: "mdi-account-tie",
        label: "LAST_NAME",
        v_model: null,
        min_length: 2,
      },
      {
        icon: "mdi-mail",
        label: "EMAIL",
        v_model: null,
        min_length: 6,
      },
      {
        icon: "mdi-lock",
        label: "PASSWORD",
        type: "password",
        v_model: null,
        min_length: 7,
      },
    ],
  },
  Licit: {
    LOGIN: [
      {
        icon: "mdi-mail",
        label: "EMAIL",
        v_model: null,
        min_length: 6,
      },
      {
        icon: "mdi-lock",
        type: "password",
        label: "PASSWORD",
        v_model: null,
        min_length: 7,
      },
    ],
    SINGUP: [
      {
        icon: "mdi-account",
        label: "FIRST_NAME",
        v_model: null,
        min_length: 2,
      },
      {
        icon: "mdi-account-tie",
        label: "LAST_NAME",
        v_model: null,
        min_length: 2,
      },
      {
        icon: "mdi-mail",
        label: "EMAIL",
        v_model: null,
        min_length: 6,
      },
      {
        icon: "mdi-lock",
        label: "PASSWORD",
        type: "password",
        v_model: null,
        min_length: 7,
      },
    ],
  },
});
