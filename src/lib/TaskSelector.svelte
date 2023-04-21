<script lang="ts">
	import { invoke } from '@tauri-apps/api/tauri';
	import Icon from '@iconify/svelte';
	import { onMount } from 'svelte';
	import { selectedTask } from '../stores';

	let stringConfig: string;
	let selected = '';
	let newChipName = '';

	selectedTask.subscribe((value) => {
		selected = value;
	});
	interface Category {
		label: string;
		color: string;
	}
	interface Config {
		categories: Category[];
	}

	const randomColor = (): string => {
		return (
			'#' + Array.from({ length: 6 }, () => Math.floor(Math.random() * 16).toString(16)).join('')
		);
	};

	let chipColor = randomColor();
	let chipArr: Category[] = [];

	onMount(async () => {
		stringConfig = await invoke('get_config');
		const config: Config = JSON.parse(stringConfig.replace(/'/g, '"'));
		chipArr = config.categories;
	});

	const inChipArr = (): boolean => chipArr.some((chip) => chip.label === newChipName);

	async function pushChipArr() {
		if (newChipName && newChipName !== 'Null' && newChipName !== 'null' && !inChipArr()) {
			invoke('check_config');
			stringConfig = await invoke('add_category', { category: newChipName, color: chipColor });
			const config: Config = JSON.parse(stringConfig.replace(/'/g, '"'));
			chipArr = config.categories;
			newChipName = '';
			chipColor = randomColor();
		}
	}

	async function removeChipArr(index: number) {
		const category = chipArr[index].label;
		invoke('check_config');
		stringConfig = await invoke('remove_category', { category });
		const config: Config = JSON.parse(stringConfig.replace(/'/g, '"'));
		chipArr = config.categories;
		selectedTask.update((n) => '');
	}

	const onKeyPress = (e: KeyboardEvent) => {
		if (e.code === 'Enter') pushChipArr();
	};
</script>

<div class="flex flex-row mb-5">
	<div class="card p-4 ml-5 flex flex-grow flex-nowrap overflow-x-auto rounded-lg">
		<div class="flex-row flex items-center justify-center pr-1"><h5>Task:</h5></div>
		{#each chipArr as c, index}
			<div
				class="chip {selected === c.label ? 'chip-selected' : 'chip-not-selected'} mx-1"
				style="--theme-color: {c.color}"
				on:click={() => selectedTask.update((n) => c.label)}
				on:keypress
			>
				{c.label}
				{#if selected !== c.label}
					<button class="ml-3" on:click={() => removeChipArr(index)}
						><Icon icon="ci:close-md" /></button
					>
				{/if}
				{#if selected === c.label}
					<div class="ml-3">
						<Icon icon="ci:check-big" />
					</div>
				{/if}
			</div>
		{/each}
	</div>
	<div class="card p-4 mx-5 basis-60 flex-none rounded-lg">
		<div class="flex flex-row items-center py-0.5">
			<input class="input rounded-md px-1" bind:value={newChipName} on:keypress={onKeyPress} />
			<input class="rounded px-1 mx-2 variant-ghost-surface" type="color" bind:value={chipColor} />
			<button type="button" class="btn btn-sm variant-filled" on:click={pushChipArr}
				><Icon icon="ci:add-plus" />
			</button>
		</div>
	</div>
</div>

<style>
	.chip-not-selected {
		background-color: var(--theme-color);
		opacity: 0.7;
		color: #ffffff;
		border-radius: 10px;
		border: var(--theme-color) 2px solid;
	}
	.chip-selected {
		background-color: var(--theme-color);
		color: #ffffff;
		border: #ffffff 2px solid;
		border-radius: 10px;
	}
</style>
