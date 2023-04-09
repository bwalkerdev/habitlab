<script lang="ts">
	import DateTimePicker from '$lib/DateTimePicker.svelte';
	import TaskSelector from '$lib/TaskSelector.svelte';
</script>

<div class="flex flex-row">
	<div class="basis-1/4 m-5"><h3>Good Morning</h3></div>
	<div class="grow" />
	<div class="basis-12 m-5"><h3>2🔥</h3></div>
</div>
<TaskSelector />
<DateTimePicker />
