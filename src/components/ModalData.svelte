<script lang="ts">
  import type { T_Todo } from "../types";
  import { modalIsOpen } from "../store";
  import { onMount } from "svelte";

  let modal: HTMLElement;

  export let data: T_Todo = {
    title: "Default title",
    importance: 0,
    text: "lorem ipsum dolor sit",
    date: new Date().toLocaleString(),
  };

  onMount(() => {
    modal.addEventListener("click", (e) => {
      const target = e.target as HTMLElement;
      const classes = Array.from(target.classList);
      if (classes.includes("modal-body")) $modalIsOpen = false;
    });
  });
</script>

<main>
  <section bind:this={modal} class="modal-body">
    <div class="modal-container">
      <div class="modal-group">
        <span>Title:</span>
        <span>{data.title}</span>
      </div>

      <div class="modal-group">
        <span>Importance:</span>
        <span>{data.importance}</span>
      </div>

      <div class="modal-group">
        <div>Text:</div>
        <textarea name="" id="" disabled>{data.text}</textarea>
      </div>
      <div class="modal-group">
        <span>Date:</span>
        <span>{data.date}</span>
      </div>
    </div>
  </section>
</main>

<style lang="scss">
  $pink: #e5b1d6;
  @mixin colored_border($wheight: 2px, $color: $pink) {
    border: $wheight solid $color;
  }
  section {
    position: absolute;
    height: 100vh;
    width: 100vw;
    top: 0%;
    background-color: #282626ae;
    z-index: 100;
    display: flex;

    .modal-container {
      background-color: #fff;
      height: 70%;
      width: 95%;
      align-self: center;
      margin-left: 2.1%;
      @include colored_border;
      border-radius: 10px;
      .modal-group {
        margin-top: 20px;
        margin-left: 5px;
        @include colored_border($wheight: 1px);
        border-radius: 5px;
        padding: 10px;
        :first-child {
          background-color: #00ff9d34;
          width: fit-content;
          padding: 2px;
        }
      }
    }
  }
</style>
