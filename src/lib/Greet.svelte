<script lang="ts">
	// When using the Tauri API npm package:
	import { invoke } from '@tauri-apps/api/tauri';
	// When using the Tauri global script (if not using the npm package)
	// Be sure to set `build.withGlobalTauri` in `tauri.conf.json` to true
	import { onMount } from 'svelte';

	let greeting = '';
	let streak: '';

	onMount(async () => {
		greeting = await invoke('py_greet');
		invoke('check_config');
		streak = await invoke('check_streak');
	});
</script>

<div class="flex flex-row">
	<div class="m-5"><h3>{greeting}</h3></div>
	<div class="grow" />
	<div class="basis-12 m-5">
		<h3 class="whitespace-nowrap">
			{#if streak}{streak}{/if}🔥
		</h3>
	</div>
</div>
