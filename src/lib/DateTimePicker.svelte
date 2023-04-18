<script lang="ts">
	import Icon from '@iconify/svelte';
	import TaskSelector from './TaskSelector.svelte';

	interface TaskTime {
		date: Date;
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
		date: new Date(0),
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
		if (
			taskTime.date &&
			taskTime.from.hour &&
			taskTime.from.AMPM &&
			taskTime.to.hour &&
			taskTime.to.AMPM
		) {
			console.log(taskTime);
		}
	};
</script>

<div class="flex flex-row">
	<div class="card p-4 mx-5 basis-60 flex-none rounded-lg">
		<label for="date">Date: </label><input
			name="date"
			id="date"
			type="date"
			bind:value={taskTime.date}
		/>
	</div>
	<div class="card p-4 flex flex-grow flex-nowrap overflow-x-auto rounded-lg">
		<div class="flex flex-col">
			<label for="from">From: </label>
			<select name="from" id="from" bind:value={taskTime.from.hour}>
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
			<select id="from-AM/PM" bind:value={taskTime.from.AMPM}>
				<option value="" disabled selected hidden>AM/PM</option>
				<option value="AM">AM</option>
				<option value="PM">PM</option>
			</select>
		</div>
		<div class="flex flex-col pl-3">
			<label for="to">To: </label>
			<select name="to" id="to" bind:value={taskTime.to.hour}>
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
				<option value="1">11:00</option>
			</select>
			<select id="to-AM/PM" bind:value={taskTime.to.AMPM}>
				<option value="" disabled selected hidden>AM/PM</option>
				<option value="AM">AM</option>
				<option value="PM">PM</option>
			</select>
		</div>
	</div>
	<div class="card p-4 mx-5 basis-40 flex-none rounded-lg">
		<button type="button" class="btn variant-filled" on:click={submitTaskTime}>
			<span><Icon icon="ci:check-big" /></span>
			<span>Submit</span>
		</button>
	</div>
</div>
