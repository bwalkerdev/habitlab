<script lang="ts">
	import { onMount } from 'svelte';
	import { invoke } from '@tauri-apps/api/tauri';

	interface Habit {
		task: string;
		color: string;
	}

	interface Day {
		[hour: string]: Habit;
	}

	interface Month {
		[day: string]: Day;
	}

	interface Year {
		[month: string]: Month;
	}

	interface Habits {
		[year: string]: Year;
	}

	interface NormalizedHabits {
		[year: string]: {
			[month: string]: {
				[day: string]: Habit;
			};
		};
	}

	let normalizedHabits: NormalizedHabits = {};

	onMount(async () => {
		const jsonString: string = await invoke('get_config');
		const jsonStringWithDoubleQuotes = jsonString.replace(/'/g, '"');
		console.log(jsonStringWithDoubleQuotes);
		let habitObj: Habits = JSON.parse(jsonStringWithDoubleQuotes).habits;
		console.log(habitObj);
		for (let key in habitObj) {
			console.log(key);
			let keyArr = key.split('-');
			// Convert the date to a Date object I have no clue why I need the -1
			const date = new Date(parseInt(keyArr[0]), parseInt(keyArr[1]) - 1, parseInt(keyArr[2]));
			if (!normalizedHabits[keyArr[0]]) {
				normalizedHabits[keyArr[0]] = {};
			}
			if (!normalizedHabits[keyArr[0]][keyArr[1]]) {
				normalizedHabits[keyArr[0]][keyArr[1]] = {};
			}
			normalizedHabits[keyArr[0]][keyArr[1]][keyArr[2]] = habitObj[key];
		}
		console.log(normalizedHabits);
	});
</script>

{#if Object.keys(normalizedHabits).length > 0}
	{#each Object.keys(normalizedHabits) as habitYear}
		<div class="card">
			<h3>{habitYear}</h3>
		</div>
	{/each}
{:else}
	<p>Loading...</p>
{/if}
