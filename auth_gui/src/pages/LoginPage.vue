<template>
  <q-page class="row">
    <div class="col-12 col-md-8 flex flex-center">
      <!--  -->
      <input-card
        v-if="context && !error"
        :information="APP_CONSTANTS.LOGIN_INFO"
        :inputs="INPUTS[currentAppName].LOGIN"
      />
      <input-card
        v-else-if="!context && !error"
        :information="APP_CONSTANTS.SIGNUP_INFO"
        :inputs="INPUTS[currentAppName].SINGUP"
      />
      <error-card v-else :error-message="error" />
    </div>
    <div class="gt-sm col-4 column flex-center bg-primary">
      <q-img v-if="!error" width="35rem" :src="AppIconSrc"></q-img>
      <div v-else class="column flex-center">
        <q-icon size="300px" name="mdi-emoticon-sad-outline"></q-icon>
        <div>Can't fetch logo! Something Went Wrong</div>
      </div>
    </div>
  </q-page>
</template>

<script>
import InputCard from "src/components/InputCard.vue";
import ErrorCard from "src/components/ErrorCard.vue";
import { computed, defineComponent, onMounted, ref } from "vue";
import { APP_CONSTANTS, COUPLED_APPS } from "src/common/constants/app";
import {
  // LOGIN_INPUTS,
  // SIGNUP_INPUTS,
  INPUTS,
} from "src/common/reactive/reactives";
import { useStore } from "vuex";

export default defineComponent({
  name: "IndexPage",
  components: {
    "input-card": InputCard,
    "error-card": ErrorCard,
  },
  setup() {
    const $store = useStore();
    let currentMode = null;
    const error = ref(null);
    const currentAppName = ref("Starks");
    const AppIconSrc = ref(null);
    //
    const context = computed(() => {
      return $store.getters["appcommons/getContext"];
    });
    //
    (() => {
      if (process.env.DEV) {
        currentMode = "local";
      } else if (process.env.PROD) {
        currentMode = "prod";
      }
    })();
    function getQueryObjectFromQS(queryString) {
      if (queryString) {
        return Object.fromEntries(new URLSearchParams(queryString));
      }
    }
    function getQueryObject() {
      let queryObject = window.location.search.substring(1);
      if (!queryObject) {
        const [, query] = window.location.href.split("#")[1].split("?");
        return getQueryObjectFromQS(query);
      }
      return getQueryObjectFromQS(queryObject);
    }
    function verifyRedirectUrl({ appTBC = null, redirectUrl = null }) {
      if (redirectUrl && currentMode) {
        return appTBC.redirect_urls_for_verification[currentMode].some(
          (redirect_verification_url) =>
            redirectUrl === redirect_verification_url
        );
      }
      return "404";
    }
    function createError(message) {
      error.value = message;
    }
    function verifyQueryProperties() {
      let queryObject = getQueryObject();
      if (!queryObject) {
        createError("Query string is missing");
        return;
      }
      const activeApp = COUPLED_APPS.find(
        (app) => app.app_name === queryObject.app_name
      );
      if (activeApp) {
        const verification = verifyRedirectUrl({
          appTBC: activeApp,
          redirectUrl: queryObject.redirect_url,
        });
        if (verification === true) {
          // Color(define and get those from thhe coupled app object)
          AppIconSrc.value = require(`../assets/icons/${activeApp.app_icon}`);
          currentAppName.value = activeApp.app_name;
          $store.commit("appcommons/setAppSettings", queryObject);
          return;
        } else if (verification === "404") {
          createError("Redirect url not Found");
          return;
        }
        createError("Incorrect redirect url");
        return;
      }
      createError("No app specified");
    }

    //
    onMounted(() => {
      verifyQueryProperties();
    });

    //
    return {
      APP_CONSTANTS,
      // LOGIN_INPUTS,
      // SIGNUP_INPUTS,
      context,
      error,
      AppIconSrc,
      INPUTS,
      currentAppName,
      //
    };
  },
});
</script>

<style lang="sass" scoped>
.logo
  max-width: 300px
  margin-bottom: 180px
</style>
