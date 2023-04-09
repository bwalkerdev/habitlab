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
	function pushChipArr() {
		chipArr = [...chipArr, { task: newChipName, color: chipColor }];
		newChipName = '';
		chipColor = randomColor();
	}
	function removeChipArr(index: number) {
		chipArr.splice(index, 1);
		chipArr = [...chipArr];
	}
</script>

<div class="flex flex-row">
	<div class="basis-1/4 m-5"><h3>Good Morning</h3></div>
	<div class="grow" />
	<div class="basis-12 m-5"><h3>2🔥</h3></div>
</div>
<div class="flex flex-row">
	<div class="card p-4 ml-5 basis-3/4">
		{#each chipArr as c, index}
			<div
				class="chip {selected === c.task
					? 'variant-soft-surface chip-selected'
					: 'chip-not-selected'} mx-1"
				style="--theme-color: {c.color}"
				on:click={() => {
					selected = c.task;
				}}
				on:keypress
			>
				{c.task}
				<button class="ml-3" on:click={() => removeChipArr(index)}
					><Icon icon="ci:close-md" /></button
				>
			</div>
		{/each}
	</div>
	<div class="card p-4 mx-5 basis-1/4">
		<div class="flex flex-row">
			<input class="input" bind:value={newChipName} />
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
		color: #ffffff;
	}
	.chip-selected {
		border-color: var(--theme-color);
		border-width: 2px;
	}
</style>
