<template>
  <q-card
    :flat="$q.screen.lt.sm ? true : false"
    class="q-pa-sm full-width card-measurements"
  >
    <q-card-section class="q-mb-sm text-h4 text-weight-bold text-grey-9">
      <div class="row">
        <div id="title">
          {{ MAP.LABELS.TITLES[information.TITLE] }}
        </div>
        <q-space></q-space>
        <div v-if="information.TITLE === 'SIGNUP'">
          <q-btn
            @click="changeContext(true)"
            round
            class="bg-primary text-white"
            icon="mdi-arrow-left-thick"
          >
            <q-tooltip anchor="center left" self="center right">
              {{ MAP.TOOL_TIPS[information.TOOL_TIP.TIP1] }}
            </q-tooltip>
          </q-btn>
        </div>
      </div>
    </q-card-section>
    <q-card-section>
      <div id="inputs" v-for="input in inputs" :key="input.label">
        <div class="q-mb-md">
          <q-input
            v-model="input.v_model"
            :label="MAP.INPUTS_LABELS[input.label]"
            :type="input?.type === 'password' ? 'password' : ''"
            :rules="[
              (val) =>
                (!!val && val.length > input.min_length) ||
                `${
                  MAP.INPUTS_LABELS[input.label]
                } is required with a minimum length of ${input.min_length}`,
            ]"
            filled
            clearable
            :ref="
              (currentInputObj) => {
                inputRefs[input.label] = currentInputObj;
              }
            "
          >
            <template #prepend>
              <q-icon :name="input.icon"></q-icon>
            </template>
          </q-input>
        </div>
      </div>
      <div v-if="information.TITLE !== 'SIGNUP'" id="forgotpass" class="row">
        <div></div>
        <q-space></q-space>
        <router-link to="">{{
          MAP.STATEMENTS[information.STATEMENTS.FORGOT_PASSWORD]
        }}</router-link>
      </div>
    </q-card-section>
    <q-card-actions class="q-mb-md column flex-center q-pa-md">
      <div id="actions" class="full-width q-mb-md">
        <q-btn
          v-if="otp !== 'verified' && information.TITLE === 'SIGNUP'"
          @click="verifyEmail"
          @keyup.enter="verifyEmail"
          class="full-width q-mb-md"
          rounded
          :label="MAP.BTN_LABELS.VERIFY"
          :loading="loadingOtp"
          color="primary"
        >
          <template #loading> <q-spinner-facebook /> </template>
        </q-btn>
        <q-btn
          v-if="
            (otp === 'verified' && information.TITLE === 'SIGNUP') ||
            information.TITLE === 'LOGIN'
          "
          @click="authenticate"
          @keyup.enter="authenticate"
          class="full-width"
          rounded
          :label="MAP.BTN_LABELS[information.BTN_LABELS.LABEL1]"
          color="primary"
        ></q-btn>
      </div>
      <div
        v-if="information.TITLE !== 'SIGNUP'"
        id="signup"
        class="column flex-center q-mt-md"
      >
        <div class="row">
          <div>{{ MAP.STATEMENTS[information.STATEMENTS.NO_ACCOUNT] }}</div>
          <router-link
            @click="changeContext(false)"
            to=""
            class="q-ml-xs text-bold"
          >
            {{ MAP.STATEMENTS[information.STATEMENTS.SIGN_UP_NOW] }}
          </router-link>
        </div>
      </div>
      <!-- <div class="q-my-md">Or</div>
      <div id="socialsignup" class="column flex-center">
        <div>
          {{ MAP.STATEMENTS[information.STATEMENTS.CREATE_ACC_WITH] }}
        </div>
        <social-btns />
      </div> -->
    </q-card-actions>
  </q-card>
</template>

<script>
// import SocialSignUp from "../components/SocialSignUp.vue";
import {
  errorNotification,
  successNotification,
} from "../common/utils/notification";
import { useQuasar } from "quasar";
import { resetInputs } from "../common/utils/functions";
import {
  computed,
  onBeforeUpdate,
  ref,
  inject,
  onMounted,
  getCurrentInstance,
} from "vue";
import { useStore } from "vuex";
import VerificationDialogVue from "./VerificationDialog.vue";
export default {
  name: "InputCard",
  props: {
    information: {
      type: Object,
      required: true,
    },
    inputs: {
      type: Object,
      required: true,
    },
  },
  components: {
    // "social-btns": SocialSignUp,
  },
  setup(props, { emit }) {
    const app = getCurrentInstance();
    const $q = useQuasar();
    const $store = useStore();
    const inputRefs = ref({});
    const verificationDialogRef = ref(null);
    let email = null;
    const loadingOtp = ref(false);
    const otp = ref(null);
    const cryoptojs = inject("cryptojs");
    let CRYPTO_CIPHER_KEY = null;
    let CRYPTO_CIPHER_IV = null;
    let OTP_LENGTH = null;

    //
    const MAP = computed(() => {
      return $store.getters["translation/getMap"];
    });
    const context = computed(() => {
      return $store.getters["appcommons/getContext"];
    });

    const appConfig = computed(() => {
      return $store.getters["appcommons/getAppConfig"];
    });
    const authDetails = computed(() => {
      return $store.getters["authentication/getAuthDetails"];
    });

    //
    function changeContext(val) {
      $store.dispatch("appcommons/toggleContext", val);
    }

    function checkInputErrors() {
      let hasError = false;
      for (let property in inputRefs.value) {
        inputRefs.value[property].validate();
        if (inputRefs.value[property].hasError) {
          hasError = true;
        }
      }
      return hasError;
    }

    const validateEmail = (email) => {
      return email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
    };

    async function verifyEmail() {
      if (checkInputErrors()) {
        return;
      }
      email = props.inputs.find((input) => input.label === "EMAIL").v_model;
      if (!validateEmail(email)) {
        errorNotification("Invalid Email!");
        return;
      }
      try {
        loadingOtp.value = true;
        const response = await $store.dispatch("authentication/verifyEmail", {
          email,
        });
        otp.value = decryptOtp(response.data.token);
        verificationDialog(otp.value);
      } catch (err) {
        errorNotification(err.data.error);
      } finally {
        loadingOtp.value = false;
      }
    }
    function decryptOtp(token) {
      let iv = CRYPTO_CIPHER_IV;
      iv = cryoptojs.enc.Utf8.parse(iv);
      let key = CRYPTO_CIPHER_KEY; //key used in backend
      key = cryoptojs.enc.Utf8.parse(key);

      let decrypted = cryoptojs.AES.decrypt(token, key, {
        iv: iv,
        mode: cryoptojs.mode.CBC,
      });
      return decrypted.toString(cryoptojs.enc.Utf8);
    }

    function verificationDialog(Otp) {
      verificationDialogRef.value = $q
        .dialog({
          component: VerificationDialogVue,
          componentProps: {
            otp: Otp,
            otpLength: OTP_LENGTH,
            otpHandlers: { resetOtp },
          },
        })
        .onOk(() => {
          otp.value = "verified";
        })
        .onCancel(() => {
          otp.value = null;
        });
    }

    async function resetOtp() {
      if (!email || !email.includes("@")) {
        errorNotification("Invalid email value!");
      }
      try {
        const response = await $store.dispatch("authentication/verifyEmail", {
          email,
        });
        otp.value = decryptOtp(response.data.token);
      } catch (err) {
        errorNotification(err);
      }
    }

    //
    async function authenticate() {
      if (checkInputErrors()) {
        return;
      }
      if (context.value) {
        const result = await $store.dispatch(
          "authentication/login",
          getPayload()
        );
        handleResponse(result, handleLoginAuth);
      } else {
        const result = await $store.dispatch(
          "authentication/signup",
          getPayload()
        );
        handleResponse(result, handleSignUpAuth);
      }
    }
    function getPayload() {
      let payloadObject = {};
      for (let index in props.inputs) {
        payloadObject[props.inputs[index].label.toLowerCase()] =
          props.inputs[index].v_model;
      }
      return payloadObject;
    }

    async function handleLoginAuth() {
      const queryStringObject = {
        auth_token: authDetails.value.auth_token,
        refresh_token: authDetails.value.refresh_token,
      };
      const queryString =
        "?" + new URLSearchParams(queryStringObject).toString();
      window.location.href = appConfig.value.redirect_url + queryString;
    }
    function handleSignUpAuth() {
      successNotification("Account created successfully");
      resetInputs("SINGUP");
      changeContext(true);
    }
    function handleResponse(result, handler) {
      if (result.status !== 200) {
        errorNotification(result.data.detail);
        return;
      }
      if (handler) {
        handler();
      }
    }

    // make sure to reset the refs before each update
    onBeforeUpdate(() => {
      inputRefs.value = [];
    });

    onMounted(() => {
      CRYPTO_CIPHER_KEY =
        app.appContext.config.globalProperties.$CRYPTO_CIPHER_KEY;
      CRYPTO_CIPHER_IV =
        app.appContext.config.globalProperties.$CRYPTO_CIPHER_IV;
      OTP_LENGTH = app.appContext.config.globalProperties.$OTP_LENGTH;
    });

    return {
      //
      MAP,
      inputRefs,
      otp,
      loadingOtp,
      //
      changeContext,
      authenticate,
      verifyEmail,
    };
  },
};
</script>
