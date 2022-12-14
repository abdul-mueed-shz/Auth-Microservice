export const APP_CONSTANTS = Object.freeze({
  TITLES: {
    LOGIN: "LOGIN",
    SIGNUP: "SIGNUP",
  },
  LOGIN_INFO: {
    TITLE: "LOGIN",
    BTN_LABELS: {
      LABEL1: "LOGIN",
    },
    TOOL_TIP: {
      TIP1: "",
    },
    STATEMENTS: {
      FORGOT_PASSWORD: "FORGOT_PASSWORD",
      SIGN_UP_NOW: "SIGN_UP_NOW",
      NO_ACCOUNT: "NO_ACCOUNT",
      CREATE_ACC_WITH: "CREATE_ACC_WITH",
    },
  },
  SIGNUP_INFO: {
    TITLE: "SIGNUP",
    BTN_LABELS: {
      LABEL1: "SIGNUP",
    },
    TOOL_TIP: {
      TIP1: "GOBACK",
    },
    STATEMENTS: {
      FORGOT_PASSWORD: "FORGOT_PASSWORD",
      SIGN_UP_NOW: "SIGN_UP_NOW",
      NO_ACCOUNT: "NO_ACCOUNT",
      CREATE_ACC_WITH: "CREATE_ACC_WITH",
    },
  },
});

export const COUPLED_APPS = [
  {
    app_name: "Starks",
    app_icon: "starks.png",
    redirect_urls_for_verification: {
      local: [
        "http://localhost:8081",
        "http://localhost:8081/#",
        "http://localhost:8081/",
        "http://localhost:8081/#/",
      ],
      prod: [""],
    },
  },
  {
    app_name: "Licit",
    app_icon: "starks.png",
    redirect_urls_for_verification: {
      local: [
        "http://localhost:8081",
        "http://localhost:8081/#",
        "http://localhost:8081/",
        "http://localhost:8081/#/",
      ],
      prod: [""],
    },
  },
];
