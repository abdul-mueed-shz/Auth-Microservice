<template>
  <q-layout view="hHh Lpr fFf">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";

export default {
  name: "BlankLayout",

  setup() {
    return {};
  },
};
</script>
