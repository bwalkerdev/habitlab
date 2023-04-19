<script lang="ts">
	// When using the Tauri API npm package:
	import { invoke } from '@tauri-apps/api/tauri';
	// When using the Tauri global script (if not using the npm package)
	// Be sure to set `build.withGlobalTauri` in `tauri.conf.json` to true
	import { onMount } from 'svelte';

	let greeting = '';
	let streak: number;

	async function getStreak() {
		await invoke('check_config');
		let stringConfig: string = await invoke('get_config');
		const config = JSON.parse(stringConfig.replace(/'/g, '"'));
		// Get current date
		const lastModified = config.meta.lastModified;
		const currentStreak = config.meta.currentStreak;
		const date = new Date();
	}

	onMount(async () => {
		greeting = await invoke('py_greet');
		// streak = await getStreak;
	});
</script>

<div class="flex flex-row">
	<div class="basis-1/4 m-5"><h3>{greeting}</h3></div>
	<div class="grow" />
	<div class="basis-12 m-5"><h3>2🔥</h3></div>
</div>
