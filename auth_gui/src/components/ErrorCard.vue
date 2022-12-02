<template>
  <q-card
    class="full-width card-measurements text-primary column flex-center q-pb-lg"
  >
    <q-card-section>
      <div>
        <a
          class="remove-underline text-primary no-underline text-weight-medium"
          :href="`mailto:${administrationEmail}`"
        >
          <q-icon
            class="cursor-pointer"
            color="negative"
            size="10rem"
            name="mdi-alert-circle"
          >
          </q-icon>
        </a>
      </div>
    </q-card-section>
    <q-card-section class="text-h4 text-weight-medium">
      {{ errorMessage }}
    </q-card-section>
    <q-card-actions class="text-h6 text-weight-regular cursor-pointer">
      <div>
        <a
          class="remove-underline text-primary no-underline text-weight-medium"
          :href="`mailto:${administrationEmail}`"
        >
          Contact Administration
        </a>
      </div>
    </q-card-actions>
  </q-card>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";

export default {
  name: "ErrorCard",
  props: {
    errorMessage: {
      type: String,
      required: true,
    },
  },
  setup() {
    const store = useStore();
    const administrationEmail = computed(() => {
      return store.getters["appcommons/getAdminEmail"];
    });
    return {
      administrationEmail,
    };
  },
};
</script>
