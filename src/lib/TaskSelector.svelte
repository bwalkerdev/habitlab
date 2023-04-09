<script lang="ts">
	import Icon from '@iconify/svelte';
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

	let chipArr = [
		{ task: 'Sleep', color: 'red' },
		{ task: 'Eat', color: 'blue' },
		{ task: 'Girlfriend', color: 'green' },
		{ task: 'School', color: 'orange' }
	];

	function inChipArr() {
		for (let i = 0; i < chipArr.length; i++) {
			if (chipArr[i].task === newChipName) {
				return true;
			}
		}
		return false;
	}

	function pushChipArr() {
		if (newChipName && newChipName != 'Null' && newChipName != 'null' && !inChipArr()) {
			chipArr = [...chipArr, { task: newChipName, color: chipColor }];
			newChipName = '';
			chipColor = randomColor();
		}
	}
	function removeChipArr(index: number) {
		chipArr.splice(index, 1);
		chipArr = [...chipArr];
	}
</script>

<div class="flex flex-row mb-5">
	<div class="card p-4 ml-5 flex flex-grow flex-nowrap overflow-x-auto rounded-lg">
		{#each chipArr as c, index}
			<div
				class="chip {selected === c.task ? 'chip-selected' : 'chip-not-selected'} mx-1"
				style="--theme-color: {c.color}"
				on:click={() => {
					selected = c.task;
				}}
				on:keypress
			>
				{c.task}
				{#if selected != c.task}
					<button class="ml-3" on:click={() => removeChipArr(index)}
						><Icon icon="ci:close-md" /></button
					>
				{/if}
				{#if selected === c.task}
					<div class="ml-3">
						<Icon icon="ci:check-big" />
					</div>
				{/if}
			</div>
		{/each}
	</div>
	<div class="card p-4 mx-5 basis-60 flex-none rounded-lg">
		<div class="flex flex-row items-center py-0.5">
			<input class="input rounded-md px-1" bind:value={newChipName} />
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
