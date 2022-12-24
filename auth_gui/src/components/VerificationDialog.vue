<template>
  <!-- notice dialogRef here -->
  <q-dialog ref="dialogRef" @hide="onDialogHide" persistent>
    <q-card class="q-dialog-plugin">
      <q-card-section>
        <div class="text-h6 text-primary">
          <div v-if="resendingOtp">Resending Otp!</div>
          <div v-else>Enter Otp to verify email</div>
        </div>
      </q-card-section>
      <q-card-section>
        <q-input
          v-model="otpModel"
          debounce="600"
          @update:model-value="verifyOTP"
          :rules="[
            (val) => isVerificationError || !!val || 'Enter otp to verify',
          ]"
          :mask="otpInputMask"
          :disable="resendingOtp"
          hint="Enter otp number"
          label="Otp"
          dense
          filled
        >
          <template #prepend>
            <q-icon name="mdi-form-textbox-password"></q-icon>
          </template>
          <template #append>
            <q-icon
              v-if="otpModel"
              class="cursor-pointer"
              name="mdi-close-circle"
              @click="clearInput"
            ></q-icon>
          </template>
        </q-input>
      </q-card-section>
      <q-card-actions align="right">
        <q-btn
          :loading="resendingOtp"
          color="primary"
          label="Resend"
          @click="resendOTP"
        >
          <template #loading> <q-spinner-facebook /> </template
        ></q-btn>
        <q-btn color="negative" label="Cancel" @click="onCancelClick" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { useDialogPluginComponent } from "quasar";
import { errorNotification } from "src/common/utils/notification";
import { ref } from "vue";

export default {
  props: {
    otp: {
      type: String,
      required: true,
    },
    otpLength: {
      type: Number,
      required: true,
    },
    otpHandlers: {
      type: Object,
      required: true,
    },
  },

  emits: [...useDialogPluginComponent.emits],

  setup(props) {
    //
    const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } =
      useDialogPluginComponent();
    const otpInputMask = "#".repeat(props.otpLength);
    const otpModel = ref(null);
    const isVerificationError = ref(null);
    const resendingOtp = ref(null);
    let verificationAttempts = 0;
    //
    function clearInput() {
      otpModel.value = null;
      isVerificationError.value = null;
    }
    async function resendOTP() {
      resendingOtp.value = true;
      await props.otpHandlers.resetOtp();
      resendingOtp.value = false;
      verificationAttempts = 0;
    }
    function verifyOTP() {
      if (!otpModel.value || otpModel.value.length < 6) {
        isVerificationError.value = null;
        return;
      }
      if (otpModel.value === props.otp) {
        onDialogOK();
        return;
      }
      isVerificationError.value = "Entered otp is incorrect!";
      if (verificationAttempts < 10) {
        verificationAttempts += 1;
        return;
      }
      errorNotification("Too many incorrect otp verification attempts");
      onDialogCancel();
    }
    return {
      dialogRef,
      otpModel,
      otpInputMask,
      isVerificationError,
      resendingOtp,

      resendOTP,
      verifyOTP,
      clearInput,
      onDialogHide,
      onOKClick() {
        onDialogOK();
      },
      onCancelClick: onDialogCancel,
    };
  },
};
</script>
