<script>
  //@ts-nocheck
  import { datas } from "../store";

</script>

<section>
  <div>
    {#each $datas as data}
      <div class="abutton">{data.title}</div>
    {/each}
  </div>
</section>

<style>
  section {
    color: white;
  }
</style>
