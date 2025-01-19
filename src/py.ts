import type { T_Py } from "./types";

export function pyLoaded(callback: (py: T_Py) => Promise<void>): T_Py {
  window.addEventListener("pywebviewready", function () {
    //@ts-ignore
    window.py = window.pywebview.api;
    //@ts-ignore
    callback(window.py).then();
  });
  //@ts-ignore
  return window.py as T_Py;
}
