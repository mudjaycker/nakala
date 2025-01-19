<script lang="ts">
  import { onMount } from "svelte";
  import List from "./components/ListReminder.svelte";
  import Navbar from "./components/NavBar.svelte";
  import { currentComponent, todos, py } from "./store";
  import { pyLoaded } from "./py";

  onMount(async () => {
    pyLoaded(async (py) => {
      $todos = await py.get()
      $py = py;
    });
    currentComponent.set(List);
  });
</script>

<main>
  <Navbar />
  <svelte:component this={$currentComponent} />
</main>
