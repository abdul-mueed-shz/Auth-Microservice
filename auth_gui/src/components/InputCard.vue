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
              (val) => !!val || `${MAP.INPUTS_LABELS[input.label]} is required`,
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
          @click="authenticate"
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
import SocialSignUp from "../components/SocialSignUp.vue";
import { computed, onBeforeUpdate, ref } from "vue";
import { useStore } from "vuex";
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
  setup(props) {
    const $store = useStore();
    const MAP = computed(() => {
      return $store.getters["translation/getMap"];
    });
    const context = computed(() => {
      return $store.getters["appcommons/getContext"];
    });
    function changeContext(val) {
      $store.dispatch("appcommons/toggleContext", val);
    }
    const inputRefs = ref({});
    function authenticate() {
      let hasError = false;
      for (let property in inputRefs.value) {
        inputRefs.value[property].validate();
        if (inputRefs.value[property].hasError) {
          hasError = true;
        }
      }
      if (hasError) {
        return;
      }
      let payload = {
        email: props.inputs.find((inp) => inp.label === "EMAIL")["v_model"],
        password: props.inputs.find((inp) => inp.label === "PASSWORD")[
          "v_model"
        ],
      };
      if (context.value) {
        $store.dispatch("authentication/login", payload);
      } else {
        const signUpSpecific = {
          first_name: props.inputs.find((inp) => inp.label === "FIRST_NAME")[
            "v_model"
          ],
          last_name: props.inputs.find((inp) => inp.label === "LAST_NAME")[
            "v_model"
          ],
        };
        payload = Object.assign(payload, signUpSpecific);
        $store.dispatch("authentication/signup", payload);
      }
    }

    // make sure to reset the refs before each update
    onBeforeUpdate(() => {
      inputRefs.value = [];
    });

    return {
      MAP,
      changeContext,
      authenticate,
      inputRefs,
    };
  },
};
</script>
