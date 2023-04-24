<script lang="ts">
	import { onMount } from 'svelte';
	import { invoke } from '@tauri-apps/api/tauri';
	import { ProgressRadial } from '@skeletonlabs/skeleton';

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
	let generatedTips: string[] = [];

	async function genTips(data: string) {
		const stringTips: string = await invoke('gen_tips', { invokeMessage: data });
		generatedTips = stringTips.split(';');
		console.log(generatedTips);
	}

	onMount(async () => {
		selectedYear = new Date().getFullYear().toString();
		const jsonStringWithDoubleQuotes = config.replace(/'/g, '"');
		let habitObj: { [date: string]: { [hour: string]: Habit } } = JSON.parse(
			jsonStringWithDoubleQuotes
		).habits;
		for (let key in habitObj) {
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
		genTips(JSON.stringify(normalizedHabits));
	});
	$: if (config) {
		const jsonStringWithDoubleQuotes = config.replace(/'/g, '"');
		let habitObj: { [date: string]: { [hour: string]: Habit } } = JSON.parse(
			jsonStringWithDoubleQuotes
		).habits;
		for (let key in habitObj) {
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
		genTips(JSON.stringify(normalizedHabits));
	}
</script>

<div>
	{#if generatedTips.length > 0}
		<div class="generated-tips card p-4 m-5 flex-row">
			<h4>AI Insights:</h4>
			<ul>
				{#each generatedTips as tip}
					<li>⦿ {tip}</li>
				{/each}
			</ul>
		</div>
	{:else}
		<div class="flex justify-center mt-5">
			<p>Loading AI Insights...</p>
			<ProgressRadial class="ml-2 mt-1" width="w-5" />
		</div>
	{/if}
</div>

<div>
	<div class="w-full flex justify-between items-start mt-5 pr-6">
		<div />
		<!-- Add an empty div as a placeholder on the left -->
		{#if Object.keys(normalizedHabits).length > 0}
			<select
				class="sticky top-0 dark:border-surface-450 rounded-lg mb-1 bg-surface-200 dark:bg-surface-600 dark:border-surface-450"
				id="habitYear"
				name="habitYear"
				on:change={() => (generatedTips = [])}
				bind:value={selectedYear}
			>
				{#each Object.keys(normalizedHabits) as habitYear}
					<option value={habitYear}>{habitYear}</option>
				{/each}
			</select>
		{:else}
			<p>Loading Visualization...</p>
			<ProgressRadial class="ml-2 mt-1" width="w-5" />
		{/if}
	</div>

	{#if selectedYear}
		{#each Object.keys(normalizedHabits[selectedYear]) as month}
			<div class="card p-4 m-5 flex flex-col">
				<h3>{months[month]} {selectedYear}</h3>
				<div class="flex mb-1">
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
											normalizedHabits[selectedYear][month][day][hour < 10 ? `0${hour}` : hour]
												.color
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
</div>
