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
		const jsonStringWithDoubleQuotes = jsonString.replace(/'/g, '"');
		try {
			const jsonData = JSON.parse(jsonStringWithDoubleQuotes);
			habits = jsonData.habits;
		} catch (error) {
			console.error('Error parsing JSON:', error);
		}
	}

	function formatHour(hour: number): string {
		const ampm = hour >= 12 ? 'PM' : 'AM';
		const formattedHour = hour % 12 || 12;
		return `${formattedHour} ${ampm}`;
	}

	function formatDay(day: string): string {
		return day.slice(5, 7);
	}
</script>

<div class="flex flex-row">
	<div class="card p-4 m-5 flex-grow rounded-lg flex items-center justify-center text-center">
		<div class="y-axis">
			{#each Object.keys(habits) as day}
				<div class="y-label">{formatDay(day)}</div>
			{/each}
		</div>
		<div class="graph">
			<div class="x-axis">
				{#each Array.from({ length: 24 }, (_, i) => i) as hour}
					<div class="x-label">{formatHour(hour)}</div>
				{/each}
			</div>
			<div class="data">
				{#each Object.keys(habits) as day}
					<div class="grid-container">
						{#each Array.from({ length: 24 }, (_, i) => i) as hour}
							{#if habits[day][`${hour}:00`]}
								<div
									class="grid-item"
									style="background-color: {habits[day][`${hour}:00`].color}"
									title={`${habits[day][`${hour}:00`].task} at ${formatHour(hour)} on ${day}`}
								/>
							{:else}
								<div class="grid-item empty" title={`No habit at ${formatHour(hour)} on ${day}`} />
							{/if}
						{/each}
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>

<style>
	.y-axis {
		display: flex;
		flex-direction: column;
	}

	.y-label {
		height: 22px;
		display: flex;
		align-items: center;
	}

	.graph {
		display: flex;
		flex-direction: column;
	}

	.x-axis {
		display: grid;
		grid-template-columns: repeat(24, 1fr);
		gap: 2px;
	}

	.x-label {
		width: 20px;
		height: 20px;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 12px;
	}

	.data {
		display: flex;
		flex-direction: column;
	}

	.grid-container {
		display: grid;
		grid-template-columns: repeat(24, 1fr);
		gap: 2px;
	}

	.grid-item {
		width: 20px;
		height: 20px;
	}

	.grid-item.empty {
		background-color: #cccccc;
	}
</style>
