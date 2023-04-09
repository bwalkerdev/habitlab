<script lang="ts">
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-crimson.css';
	// If you have source.organizeImports set to true in VSCode, then it will auto change this ordering
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../app.postcss';
	import { AppShell, AppBar, AppRail, AppRailTile } from '@skeletonlabs/skeleton';
	import { writable } from 'svelte/store';
	import type { Writable } from 'svelte/store';
	const storeValue: Writable<number> = writable(0);
	import Icon from '@iconify/svelte';
	import { LightSwitch } from '@skeletonlabs/skeleton';
</script>

<AppShell>
	<svelte:fragment slot="sidebarLeft">
		<AppRail width="w-[80px]" selected={storeValue} class="rounded-r-lg">
			<AppRailTile value={0}><Icon icon="ci:house-01" width="35" height="35" /></AppRailTile>
			<AppRailTile value={1}><Icon icon="ci:table" width="35" height="35" /></AppRailTile>
			<AppRailTile value={2}><Icon icon="ci:settings" width="35" height="35" /></AppRailTile>
			<svelte:fragment slot="trail"><LightSwitch class="mx-4 my-5" /></svelte:fragment>
		</AppRail>
	</svelte:fragment>
	<!-- Router Slot -->
	<slot />
	<!-- ---- / ---- -->
</AppShell>
