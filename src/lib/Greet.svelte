<script lang="ts">
	// When using the Tauri API npm package:
	import { invoke } from '@tauri-apps/api/tauri';
	// When using the Tauri global script (if not using the npm package)
	// Be sure to set `build.withGlobalTauri` in `tauri.conf.json` to true
	import { onMount } from 'svelte';

	let greeting = '';

	onMount(async () => {
		greeting = await invoke('py_greet');
	});
</script>

<div class="flex flex-row">
	<div class="basis-1/4 m-5"><h3>{greeting}</h3></div>
	<div class="grow" />
	<div class="basis-12 m-5"><h3>2🔥</h3></div>
</div>
