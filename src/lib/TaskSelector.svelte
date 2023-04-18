<script lang="ts">
	import { invoke } from '@tauri-apps/api/tauri';
	import Icon from '@iconify/svelte';
	import { onMount } from 'svelte';

	interface Category {
		label: string;
		color: string;
	}
	interface Config {
		categories: Category[];
	}

	let stringConfig: string;
	let selected = '';
	let newChipName = '';

	let randomColor = () => {
		let color = '#';
		for (let i = 0; i < 6; i++) {
			color += Math.floor(Math.random() * 16).toString(16);
		}
		return color;
	};

	let chipColor = randomColor();

	let chipArr: Category[] = [];

	onMount(async () => {
		stringConfig = await invoke('get_config');
		let config: Config = JSON.parse(stringConfig.replace(/'/g, '"'));
		chipArr = config.categories;
	});

	function inChipArr() {
		for (let i = 0; i < chipArr.length; i++) {
			if (chipArr[i].label === newChipName) {
				return true;
			}
		}
		return false;
	}

	async function pushChipArr() {
		if (newChipName && newChipName != 'Null' && newChipName != 'null' && !inChipArr()) {
			invoke('check_config');
			// Test push to python
			stringConfig = await invoke('add_category', {
				category: newChipName,
				color: chipColor
			});
			let config: Config = JSON.parse(stringConfig.replace(/'/g, '"'));
			console.log(stringConfig);
			chipArr = config.categories;
			newChipName = '';
			chipColor = randomColor();
		}
	}
	async function removeChipArr(index: number) {
		let category = chipArr[index].label;
		invoke('check_config');
		stringConfig = await invoke('remove_category', {
			category: category
		});
		let config: Config = JSON.parse(stringConfig.replace(/'/g, '"'));
		chipArr = config.categories;
	}
	const onKeyPress = (e: KeyboardEvent) => {
		if (e.code === 'Enter') pushChipArr();
	};
</script>

<div class="flex flex-row mb-5">
	<div class="card p-4 ml-5 flex flex-grow flex-nowrap overflow-x-auto rounded-lg">
		{#each chipArr as c, index}
			<div
				class="chip {selected === c.label ? 'chip-selected' : 'chip-not-selected'} mx-1"
				style="--theme-color: {c.color}"
				on:click={() => {
					selected = c.label;
				}}
				on:keypress
			>
				{c.label}
				{#if selected != c.label}
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
				><Icon icon="ci:add-plus" /></button
			>
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
	/* width */
	::-webkit-scrollbar {
		height: 5px;
	}

	/* Track */
	::-webkit-scrollbar-track {
		background: #f1f1f1;
	}

	/* Handle */
	::-webkit-scrollbar-thumb {
		background: #888;
	}

	/* Handle on hover */
	::-webkit-scrollbar-thumb:hover {
		background: #555;
	}
</style>
