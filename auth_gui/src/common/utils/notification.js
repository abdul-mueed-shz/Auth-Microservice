// outside of a Vue file
import { Notify } from "quasar";

export function successNotification(message) {
  Notify.create({
    position: "top",
    type: "positive",
    message,
    timeout: 2000,
  });
}

export function errorNotification(message) {
  Notify.create({
    position: "top",
    type: "negative",
    message,
    timeout: 2000,
  });
}

export function infoNotification(message) {
  //
}
