<script lang="ts">
  import { todos } from "../store";
  import type { T_Todo } from "../types";
  import ModalData from "./ModalData.svelte";
  import { modalIsOpen } from "../store";

  let selectedTodo: T_Todo = $todos[0];

  const showTodo = (todo: T_Todo) => {
    $modalIsOpen = true;
    selectedTodo = todo;
  };
</script>

<main>
  <section id="main">
    <div>
      {#each $todos as todo}
        <section id="reminder">
          <div id="title">{todo.title}</div>
          <div class="buttons">
            <button class="jbutton button">del</button>
            <button class="jbutton button">end</button>
            <button class="jbutton button" on:click={() => showTodo(todo)}
              >See</button
            >
          </div>
        </section>
      {/each}
    </div>
  </section>
  {#if $modalIsOpen}
    <ModalData data={selectedTodo} />
  {/if}
</main>

<style lang="scss">
  #main {
    margin-bottom: 15px;
  }
  #reminder {
    display: flex;
    justify-content: space-between;
    background-color: #bfb8cb;
    padding-left: 20px;
    padding-right: 20px;
    // border-bottom: 1px solid #000;
    margin-top: 15px;
    width: 80%;
    margin-left: 3%;
    #title {
      color: #3e3b3b;
      font-weight: 600;
      font-size: small;
      border-bottom: 0;
      margin-top: 10px;
    }
    .buttons {
      display: flex;
      justify-content: space-between;
      .button {
        margin-left: 10px;
        width: 90px;
        height: 80%;
        margin-top: 2%;
      }
      :first-child {
        background-color: #f24f4f;
        color: white;
      }
      :nth-child(2) {
        background-color: #eee18c;
        // color: white;
      }
    }
  }
</style>
