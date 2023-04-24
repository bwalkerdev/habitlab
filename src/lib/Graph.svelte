<script lang="ts">
	import { onMount } from 'svelte';
	import { invoke } from '@tauri-apps/api/tauri';

	export let config = '';

	type MonthNames = {
		[key: string]: string;
		'01': string;
		'02': string;
		'03': string;
		'04': string;
		'05': string;
		'06': string;
		'07': string;
		'08': string;
		'09': string;
		'10': string;
		'11': string;
		'12': string;
	};

	const months: MonthNames = {
		'01': 'January',
		'02': 'February',
		'03': 'March',
		'04': 'April',
		'05': 'May',
		'06': 'June',
		'07': 'July',
		'08': 'August',
		'09': 'September',
		'10': 'October',
		'11': 'November',
		'12': 'December'
	};

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

	interface NormalizedHabits {
		[year: string]: {
			[month: string]: Month;
		};
	}

	let normalizedHabits: NormalizedHabits = {};
	let selectedYear = '';

	onMount(async () => {
		const jsonString: string = await invoke('get_config');
		const jsonStringWithDoubleQuotes = jsonString.replace(/'/g, '"');
		console.log(jsonStringWithDoubleQuotes);
		let habitObj: { [date: string]: { [hour: string]: Habit } } = JSON.parse(
			jsonStringWithDoubleQuotes
		).habits;
		console.log(habitObj);
		for (let key in habitObj) {
			console.log(key);
			let keyArr = key.split('-');
			const year = keyArr[0];
			const month = keyArr[1];
			const day = keyArr[2];

			if (!normalizedHabits[year]) {
				normalizedHabits[year] = {};
			}
			if (!normalizedHabits[year][month]) {
				normalizedHabits[year][month] = {};
			}
			normalizedHabits[year][month][day] = habitObj[key];
		}
		console.log(normalizedHabits);
	});
</script>

<div class="flex flex-col justify-center items-center">
	{#if Object.keys(normalizedHabits).length > 0}
		<label for="habitYear">Select habit year:</label>
		<select id="habitYear" name="habitYear" bind:value={selectedYear}>
			{#each Object.keys(normalizedHabits) as habitYear}
				<option value={habitYear}>{habitYear}</option>
			{/each}
		</select>
	{:else}
		<p>Loading...</p>
	{/if}
</div>

{#if selectedYear}
	{#each Object.keys(normalizedHabits[selectedYear]) as month}
		<div class="card p-4 m-5 flex flex-col">
			<h3>{months[month]} {selectedYear}</h3>
			<div class="flex mb-4">
				<div class="w-8" />
				{#each Array.from({ length: 24 }, (_, i) => i) as hour}
					<div class="w-6 text-center mr-2">{hour < 10 ? `0${hour}` : hour}</div>
				{/each}
			</div>
			{#each Object.keys(normalizedHabits[selectedYear][month]) as day}
				<div class="flex items-center">
					<div class="w-8 text-right mr-2">{day}</div>
					{#each Array.from({ length: 24 }, (_, i) => i) as hour}
						<div
							class="w-6 h-6 bg-gray-600 mr-2 mb-2"
							style={normalizedHabits[selectedYear][month][day][hour < 10 ? `0${hour}` : hour]
								? `background-color: ${
										normalizedHabits[selectedYear][month][day][hour < 10 ? `0${hour}` : hour].color
								  }`
								: ''}
							title={normalizedHabits[selectedYear][month][day][hour < 10 ? `0${hour}` : hour]
								? `${
										normalizedHabits[selectedYear][month][day][hour < 10 ? `0${hour}` : hour].task
								  }\n${selectedYear}-${month}-${day}\n${hour < 10 ? `0${hour}` : hour}:00`
								: ''}
						/>
					{/each}
				</div>
			{/each}
		</div>
	{/each}
{/if}
