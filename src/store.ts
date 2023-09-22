import { writable } from "svelte/store";

export let currentComponent = writable(undefined)
export let datas = writable([])