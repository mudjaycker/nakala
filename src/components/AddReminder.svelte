<script lang="ts">
  import { todos, py } from "../store";
  import type { T_Todo } from "../types";

  let reminder = {
    title: "",
    text: "",
    importance: 0,
  };
  const save = function (data: T_Todo) {
    data.importance = Number(data.importance)
    $py.create(data)
      .then(() => {
        alert("Success");
        $todos.push(data);
      })
      .catch((e) => {
        alert(e);
      });
  };
</script>

<section>
  <div class="form__group field">
    <input
      type="input"
      class="form__field"
      placeholder="Today's todo"
      required
      bind:value={reminder.title}
    />
    <label for="name" class="form__label">Today's todo</label>
  </div>
  <div>
    <select bind:value={reminder.importance}>
      <option value="0">Low</option>
      <option value="1">Normal</option>
      <option value="2">High</option>
    </select>
  </div>

  <div id="wrapper">
    <form id="paper" method="get" action="">
      <textarea
        placeholder="Enter something funny."
        id="text"
        name="text"
        bind:value={reminder.text}
        style="overflow: hidden; word-wrap: break-word; resize: none; height: 160px; width: 30%"
      />
      <br />
    </form>
    <button class="jbutton" type="button" on:click={()=>save(reminder)}>Add</button>
  </div>
</section>

<style lang="scss">
  section {
    width: 100%;
    height: 100%;
    margin-top: 40px;
    margin-left: 1%;
  }
  .form__group {
    width: 96.2%;
  }
  input {
    color: black;
  }
</style>
