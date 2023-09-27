<script lang="ts">
  //@ts-nocheck
  import { currentComponent } from "../store";
  import List from "./ListReminder.svelte";
  import Add from "./AddReminder.svelte";

  let count: number = 0;
</script>

<section>
  <nav>
    <button
      class="mbutton"
      on:click={async () => {
        $currentComponent = Add;
      }}
    >
      Add reminder
    </button>
    <button
      class="mbutton"
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
    background: none;
    display: flex;
    justify-content: space-between;
    border: 5px double var(--color1);
    padding: 10px;
    flex-direction: row;
  }
</style>
