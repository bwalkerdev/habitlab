<script lang="ts">
	import Icon from '@iconify/svelte';
	import { selectedTask } from '../stores';

	let selectedChip: string;
	let buttonColor = 'bg-surface-800';
	let buttonIcon = 'ci:check-big';
	let dateColor = 'bg-surface-200 dark:bg-surface-600 dark:border-surface-450';

	function checkDateColor() {
		if (taskTime.date) {
			dateColor = 'bg-lime-600';
		} else {
			dateColor = 'bg-surface-200 dark:bg-surface-600 dark:border-surface-450';
		}
	}

	selectedTask.subscribe((value) => {
		selectedChip = value;
	});

	interface TaskTime {
		task: string;
		date: Date | null;
		from: {
			hour: string;
			AMPM: string;
		};
		to: {
			hour: string;
			AMPM: string;
		};
	}

	var globalDate: Date;

	let taskTime: TaskTime = {
		task: '',
		date: null,
		from: {
			hour: '',
			AMPM: ''
		},
		to: {
			hour: '',
			AMPM: ''
		}
	};

	const submitTaskTime = () => {
		taskTime.task = selectedChip;
		if (
			taskTime.task &&
			taskTime.date &&
			taskTime.from.hour &&
			taskTime.from.AMPM &&
			taskTime.to.hour &&
			taskTime.to.AMPM
		) {
			buttonColor = 'bg-success-800';
			buttonIcon = 'ci:file-upload';
			console.log(taskTime);
			setTimeout(() => {
				buttonColor = 'bg-surface-800';
				buttonIcon = 'ci:check-big';
			}, 750);
		} else {
			buttonColor = 'bg-error-800';
			buttonIcon = 'ci:close-big';
			setTimeout(() => {
				buttonColor = 'bg-surface-800';
				buttonIcon = 'ci:check-big';
			}, 500);
		}
	};
	let fromColor: string;
	let toColor: string;

	let changeFromColor = () => {
		if (taskTime.from.AMPM === 'AM') {
			fromColor = 'bg-secondary-500 text-white';
		} else if (taskTime.from.AMPM === 'PM') {
			fromColor = 'bg-amber-900 text-white';
		} else {
			fromColor = 'bg-gray-500';
		}
	};

	let changeToColor = () => {
		if (taskTime.to.AMPM === 'AM') {
			toColor = 'bg-secondary-500 text-white';
		} else if (taskTime.to.AMPM === 'PM') {
			toColor = 'bg-amber-900 text-white';
		} else {
			toColor = 'bg-gray-500';
		}
	};
</script>

<div class="flex flex-row">
	<div class="card p-4 mx-5 basis-60 flex-none rounded-lg flex items-center justify-center">
		<div class="flex-col align-middle text-center content-center">
			<h4>On which day?</h4>
			<input
				name="date"
				id="date"
				type="date"
				bind:value={taskTime.date}
				class="animated {dateColor} rounded"
				on:change={checkDateColor}
			/>
		</div>
	</div>
	<div class="card p-4 flex flex-grow flex-nowrap overflow-x-auto rounded-lg">
		<div class="flex-col basis-4 pr-5 flex items-center justify-center">
			<h4>At What Time?</h4>
		</div>
		<div class="flex flex-col text-center">
			<label for="from">From: </label>
			<select
				id="from-AM/PM"
				bind:value={taskTime.from.AMPM}
				on:change={() => changeFromColor()}
				class="{fromColor} animated"
			>
				<option value="" disabled selected hidden>AM/PM</option>
				<option value="AM">AM</option>
				<option value="PM">PM</option>
			</select>
			<select name="from" id="from" bind:value={taskTime.from.hour} class="animated {fromColor}">
				<option value="" disabled selected hidden>Start Hour</option>
				<option value="12">12:00</option>
				<option value="1">1:00</option>
				<option value="2">2:00</option>
				<option value="3">3:00</option>
				<option value="4">4:00</option>
				<option value="5">5:00</option>
				<option value="6">6:00</option>
				<option value="7">7:00</option>
				<option value="8">8:00</option>
				<option value="9">9:00</option>
				<option value="10">10:00</option>
				<option value="11">11:00</option>
			</select>
		</div>
		<div class="flex flex-col pl-3 text-center">
			<label for="to">To: </label>
			<select
				id="to-AM/PM"
				bind:value={taskTime.to.AMPM}
				on:change={() => changeToColor()}
				class="{toColor} animated"
			>
				<option value="" disabled selected hidden>AM/PM</option>
				<option value="AM">AM</option>
				<option value="PM">PM</option>
			</select>
			<select name="to" id="to" bind:value={taskTime.to.hour} class="{toColor} animated">
				<option value="" disabled selected hidden>End Hour</option>
				<option value="12">12:00</option>
				<option value="1">1:00</option>
				<option value="2">2:00</option>
				<option value="3">3:00</option>
				<option value="4">4:00</option>
				<option value="5">5:00</option>
				<option value="6">6:00</option>
				<option value="7">7:00</option>
				<option value="8">8:00</option>
				<option value="9">9:00</option>
				<option value="10">10:00</option>
				<option value="11">11:00</option>
			</select>
		</div>
	</div>
	<div class="card p-4 mx-5 basis-20 flex-none rounded-lg flex items-center justify-center">
		<button type="button" class="btn variant-filled {buttonColor}" on:click={submitTaskTime}>
			<span><Icon icon={buttonIcon} /></span>
			<span>Submit</span>
		</button>
	</div>
</div>

<style>
	.animated {
		transition: background-color 0.25s ease;
	}
</style>
