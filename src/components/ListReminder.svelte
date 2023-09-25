<script>
  //@ts-nocheck
  import { datas } from "../store";

</script>

<section>
  <ul>
    {#each $datas as data}
      <li>{data.title}</li>
    {/each}
  </ul>
</section>

<style>
  section {
    color: white;
  }
</style>
