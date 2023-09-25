<script lang="ts">
  //@ts-nocheck
  import { onMount } from "svelte";
  import List from "./components/ListReminder.svelte";
  import Navbar from "./components/NavBar.svelte";
  import { currentComponent, datas } from "./store";
  import { py } from "./var";

  onMount(async () => {
    currentComponent.set(List);
    $datas = await py.get()
  });
</script>

<main>
  <Navbar />
  <svelte:component this={$currentComponent} />
</main>
