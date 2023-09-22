<script lang="ts">
  //@ts-nocheck
  import { currentComponent } from "../store";
  import List from "./ListReminder.svelte";
  import Add from "./AddReminder.svelte";

  let count: number = 0;
  const increment = () => {
    count += 1;
  };
</script>

<section>
  <nav>
    <button
      on:click={() => {
        $currentComponent = Add;
      }}
    >
      Add reminder
    </button>
    <button
      on:click={() => {
        $currentComponent = List;
      }}
    >
      Reminder list
    </button>
  </nav>
</section>

<style>
  nav {
    background: var(--color1);
    display: flex;
    justify-content: space-between;
  }
</style>
