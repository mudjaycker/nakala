<script>
  //@ts-nocheck
  import { datas } from "../store";
  import { onMount } from "svelte";
  import { py } from "../var";

  onMount(async ()=>{
    $datas = await py.get_reminders()
  })
</script>

<section>
  <ul>
    {#each $datas as data}
      <li>{data?.title}</li>
    {/each}
  </ul>
</section>

<style>
  section {
    color: white;
  }
</style>
