<script lang="ts">
	import Icon from '@iconify/svelte';
	import { selectedTask, selectedColor } from '../stores';
	import { invoke } from '@tauri-apps/api/tauri';

	let selectedChip: string;
	let colorSelected: string;
	let buttonColor = 'bg-surface-800';
	let buttonIcon = 'ci:check-big';
	let startDateColor = 'bg-surface-200 dark:bg-surface-600 dark:border-surface-450';
	let endDateColor = 'bg-surface-200 dark:bg-surface-600 dark:border-surface-450';
	let config = '';

	function checkStartDateColor() {
		if (habit.from.date) {
			startDateColor = 'bg-lime-600';
		} else {
			startDateColor = 'bg-surface-200 dark:bg-surface-600 dark:border-surface-450';
		}
	}

	function checkEndDateColor() {
		if (habit.to.date) {
			endDateColor = 'bg-lime-600';
		} else {
			endDateColor = 'bg-surface-200 dark:bg-surface-600 dark:border-surface-450';
		}
	}

	selectedTask.subscribe((value) => {
		selectedChip = value;
	});
	selectedColor.subscribe((value) => {
		colorSelected = value;
	});

	interface Habit {
		task: string;
		color: string;
		from: {
			date: Date | null;
			hour: string;
			AMPM: string;
		};
		to: {
			date: Date | null;
			hour: string;
			AMPM: string;
		};
	}

	var globalDate: Date;

	let habit: Habit = {
		task: '',
		color: '',
		from: {
			date: null,
			hour: '',
			AMPM: ''
		},
		to: {
			date: null,
			hour: '',
			AMPM: ''
		}
	};

	const submitHabit = async () => {
		habit.task = selectedChip;
		habit.color = colorSelected;
		if (
			habit.task &&
			habit.from.date &&
			habit.to.date &&
			habit.from.hour &&
			habit.from.AMPM &&
			habit.to.hour &&
			habit.to.AMPM
		) {
			buttonColor = 'bg-success-800 dark:bg-success-800';
			buttonIcon = 'ci:check-all-big';
			let habitString = JSON.stringify(habit);
			console.log(habitString);
			config = await invoke('add_habit_to_file', { habit: habitString });
			setTimeout(() => {
				buttonColor = 'bg-surface-800';
				buttonIcon = 'ci:check-big';
			}, 750);
		} else {
			buttonColor = 'bg-error-800 dark:bg-error-800';
			buttonIcon = 'ci:close-big';
			setTimeout(() => {
				buttonColor = 'bg-surface-800';
				buttonIcon = 'ci:check-big';
			}, 500);
		}
	};
	let fromColor = 'bg-surface-200 dark:bg-surface-600 ';
	let toColor = 'bg-surface-200 dark:bg-surface-600 ';

	let changeFromColor = () => {
		if (habit.from.AMPM === 'AM') {
			fromColor = 'bg-secondary-500 text-white';
		} else if (habit.from.AMPM === 'PM') {
			fromColor = 'bg-amber-900 text-white';
		}
	};

	let changeToColor = () => {
		if (habit.to.AMPM === 'AM') {
			toColor = 'bg-secondary-500 text-white';
		} else if (habit.to.AMPM === 'PM') {
			toColor = 'bg-amber-900 text-white';
		}
	};
</script>

<div class="flex flex-row">
	<div class="card p-4 mx-5 basis-60 flex-none rounded-lg flex items-center justify-center">
		<div class="flex-col align-middle text-center content-center">
			<h4>On which day?</h4>
			<h6>Start:</h6>
			<input
				name="start-date"
				id="start-date"
				type="date"
				bind:value={habit.from.date}
				class="animated {startDateColor} rounded"
				on:change={checkStartDateColor}
			/>
			<h6>End:</h6>
			<input
				name="start-date"
				id="start-date"
				type="date"
				bind:value={habit.to.date}
				class="animated {endDateColor} rounded"
				on:change={checkEndDateColor}
			/>
		</div>
	</div>
	<div class="card p-4 flex flex-grow flex-nowrap overflow-x-auto rounded-lg">
		<div class="flex-col basis-4 pr-5 flex items-center justify-center">
			<h4>At What Time?</h4>
		</div>
		<div class="flex flex-col text-center align-middle justify-center items-center">
			<label for="from">From: </label>
			<select
				id="from-AM/PM"
				bind:value={habit.from.AMPM}
				on:change={() => changeFromColor()}
				class="{fromColor} animated dark:border-surface-450 rounded-lg mb-1"
			>
				<option value="" disabled selected hidden>AM/PM</option>
				<option value="AM">AM</option>
				<option value="PM">PM</option>
			</select>
			<select
				name="from"
				id="from"
				bind:value={habit.from.hour}
				class="{fromColor} animated dark:border-surface-450 rounded-lg"
			>
				<option value="" disabled selected hidden>Start Hour</option>
				<option value="12">12:00 {habit.from.AMPM}</option>
				<option value="1">1:00 {habit.from.AMPM}</option>
				<option value="2">2:00 {habit.from.AMPM}</option>
				<option value="3">3:00 {habit.from.AMPM}</option>
				<option value="4">4:00 {habit.from.AMPM}</option>
				<option value="5">5:00 {habit.from.AMPM}</option>
				<option value="6">6:00 {habit.from.AMPM}</option>
				<option value="7">7:00 {habit.from.AMPM}</option>
				<option value="8">8:00 {habit.from.AMPM}</option>
				<option value="9">9:00 {habit.from.AMPM}</option>
				<option value="10">10:00 {habit.from.AMPM}</option>
				<option value="11">11:00 {habit.from.AMPM}</option>
			</select>
		</div>
		<div class="flex flex-col pl-3 text-center align-middle justify-center items-center">
			<label for="to">To: </label>
			<select
				id="to-AM/PM"
				bind:value={habit.to.AMPM}
				on:change={() => changeToColor()}
				class="{toColor} animated dark:border-surface-450 rounded-lg mb-1"
			>
				<option value="" disabled selected hidden>AM/PM</option>
				<option value="AM">AM</option>
				<option value="PM">PM</option>
			</select>
			<select
				name="to"
				id="to"
				bind:value={habit.to.hour}
				class="{toColor} animated dark:border-surface-450 rounded-lg"
			>
				<option value="" disabled selected hidden>End Hour</option>
				<option value="12">12:00 {habit.to.AMPM}</option>
				<option value="1">1:00 {habit.to.AMPM}</option>
				<option value="2">2:00 {habit.to.AMPM}</option>
				<option value="3">3:00 {habit.to.AMPM}</option>
				<option value="4">4:00 {habit.to.AMPM}</option>
				<option value="5">5:00 {habit.to.AMPM}</option>
				<option value="6">6:00 {habit.to.AMPM}</option>
				<option value="7">7:00 {habit.to.AMPM}</option>
				<option value="8">8:00 {habit.to.AMPM}</option>
				<option value="9">9:00 {habit.to.AMPM}</option>
				<option value="10">10:00 {habit.to.AMPM}</option>
				<option value="11">11:00 {habit.to.AMPM}</option>
			</select>
		</div>
	</div>
	<div class="card p-4 mx-5 basis-20 flex-none rounded-lg flex items-center justify-center">
		<button type="button" class="btn variant-filled {buttonColor}" on:click={submitHabit}>
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
