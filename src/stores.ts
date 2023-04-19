import { writable } from "svelte/store";

export const selectedTask = writable<string>("");