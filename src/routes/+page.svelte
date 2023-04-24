<script lang="ts">
	import DateTimePicker from '$lib/DateTimePicker.svelte';
	import Graph from '$lib/Graph.svelte';
	import Greet from '$lib/Greet.svelte';
	import TaskSelector from '$lib/TaskSelector.svelte';
	import { invoke } from '@tauri-apps/api/tauri';
	import { onMount } from 'svelte';

	let config = '';

	async function refreshConfig() {
		config = await invoke('get_config');
	}

	onMount(async () => {
		config = await invoke('get_config');
	});
</script>

<Greet />
<TaskSelector />
<DateTimePicker on:configupdated={refreshConfig} />
<Graph {config} />
