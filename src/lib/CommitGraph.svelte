<script lang="ts">
	import { onMount } from 'svelte';
	import type { Readable } from 'svelte/store';
	import { invoke } from '@tauri-apps/api/tauri';

	type Habit = {
		[day: string]: {
			[hour: string]: { task: string; color: string };
		};
	};

	let habits: Habit = {};
	let jsonString: string;

	onMount(async () => {
		try {
			jsonString = await invoke('get_config');
		} catch (error) {
			console.error('Error invoking config:', error);
		}
	});

	$: if (jsonString) {
		console.log('JSON String:', jsonString);
		const jsonStringWithDoubleQuotes = jsonString.replace(/'/g, '"'); // Add this line
		try {
			const jsonData = JSON.parse(jsonStringWithDoubleQuotes); // Change this line
			habits = jsonData.habits;
		} catch (error) {
			console.error('Error parsing JSON:', error);
		}
	}
</script>

<div>
	{#each Object.keys(habits) as day}
		<div class="grid-container">
			{#each Object.keys(habits[day]) as hour}
				<div
					class="grid-item"
					style="background-color: {habits[day][hour].color}"
					title={habits[day][hour].task}
				/>
			{/each}
		</div>
	{/each}
</div>

<style>
	.grid-container {
		display: grid;
		grid-template-columns: repeat(24, 1fr);
		gap: 2px;
	}

	.grid-item {
		width: 20px;
		height: 20px;
	}
</style>
