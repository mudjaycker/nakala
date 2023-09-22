<script lang="ts">
  //@ts-nocheck
  import { currentComponent } from "../store";
  import List from "./List.svelte";
  import ReminderField from "./ReminderField.svelte";

  let count: number = 0;
  const increment = () => {
    count += 1;
  };
</script>

<section>
  <nav>
    <button
      on:click={() => {
        $currentComponent = ReminderField;
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
