<template>
  <q-page class="row">
    <div class="col-12 col-md-8 flex flex-center">
      <!--  -->
      <input-card
        v-if="context"
        :information="APP_CONSTANTS.LOGIN_INFO"
        :inputs="LOGIN_INPUTS"
      ></input-card>
      <input-card
        v-else
        :information="APP_CONSTANTS.SIGNUP_INFO"
        :inputs="LOGIN_INPUTS"
      ></input-card>
    </div>
    <div class="gt-sm col-4 bg-primary"></div>
  </q-page>
</template>

<script>
import InputCard from "src/components/InputCard.vue";
import { computed, defineComponent } from "vue";
import { APP_CONSTANTS } from "src/common/constants/app";
import { LOGIN_INPUTS } from "src/common/reactive/reactives";
import { useStore } from "vuex";

export default defineComponent({
  name: "IndexPage",
  components: {
    "input-card": InputCard,
  },
  setup() {
    const $store = useStore();
    const context = computed(() => {
      return $store.getters["appcommons/getContext"];
    });
    return {
      APP_CONSTANTS,
      LOGIN_INPUTS,
      context,
    };
  },
});
</script>

<style lang="sass" scoped>
.card-measurements
  max-width: 750px
</style>
