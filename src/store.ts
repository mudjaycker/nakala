import { writable } from "svelte/store";
import type { T_Py, T_Todo } from "./types";
import type ListReminder from "./components/ListReminder.svelte";

export let currentComponent = writable<typeof ListReminder>();
export let todos = writable<T_Todo[]>([]);
export let py = writable<T_Py>();
export let modalIsOpen = writable<boolean>(false);
