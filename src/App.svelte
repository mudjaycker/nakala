<script lang="ts">
  //@ts-nocheck
  import { onMount } from "svelte";
  import List from "./components/ListReminder.svelte";
  import Navbar from "./components/NavBar.svelte";
  import { currentComponent } from "./store";

  onMount(() => {
    currentComponent.set(List);
  });
</script>

<main>
  <Navbar />
  <svelte:component this={$currentComponent} />
</main>
