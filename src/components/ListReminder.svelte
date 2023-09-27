<script>
  //@ts-nocheck
  import { datas } from "../store";
</script>

<section id="main">
  <div>
    {#each $datas as data}
      <section id="reminder">
        <div id="title">{data.title}</div>
        <button class="mbutton">See</button>
      </section>
    {/each}
  </div>
</section>

<style lang="scss">
  #main{
    margin-bottom: 15px;
  }
  #reminder {
    display: flex;
    justify-content: space-between;
    background-color: #bfb8cb;
    padding-left: 20px;
    padding-right: 20px;
    border-bottom: 1px solid #000;
    margin-top: 15px;
    #title {
      color: #3e3b3b;
      font-weight: 600;
      font-size: larger;
      border-bottom: 0;
      margin-top: 10px;
    }
  }
</style>
