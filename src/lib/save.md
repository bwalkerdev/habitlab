/ * 
{#if selectedYear}
	{#each Object.keys(normalizedHabits[selectedYear]) as month}
		<div class="card p-4 m-5 flex">
			<h3>{months[month]} {selectedYear}</h3>
			<div class="grid grid-cols-24 gap-1">
				{#each Array.from({ length: 24 }, (_, i) => i) as hour}
					<div>
						<p>Hour: {hour < 10 ? `0${hour}` : hour}</p>
					</div>
				{/each}

				{#each Object.keys(normalizedHabits[selectedYear][month]) as day}
					<h4>Day: {day}</h4>
					{#each Object.keys(normalizedHabits[selectedYear][month][day]) as hour}
						<p>
							Hour: {hour} - Task: {normalizedHabits[selectedYear][month][day][hour].task} - Color: {normalizedHabits[
								selectedYear
							][month][day][hour].color}
						</p>
					{/each}
				{/each}
			</div>
		</div>
	{/each}
{/if}
 */