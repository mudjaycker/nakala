<script>
  //@ts-nocheck
  import { py } from "../var";

  let reminder = {
    title: "",
    text: "",
  };
  $: save = function () {
    py.create_reminder(reminder)
      .then(() => {
        alert("Success");
        reminder.text = "";
        reminder.title = "";
      })
      .catch((e) => {
        alert(e);
      });
  };
</script>

<section>
  <div>
    <input type="text" placeholder="Title" bind:value={reminder.title} />
    <textarea name="" id="" cols="28" rows="8" bind:value={reminder.text} />
    <button type="button" on:click={save}>add</button>
  </div>
</section>

<style>
  section {
    width: 100%;
    height: 100%;
    margin-top: 40px;
    margin-left: 1%;
  }
  textarea {
    width: 96.2%;
    margin-top: 2%;
    background-color: var(--color2);
    margin-top: 40px;
    font-size: large;
    border: 2px double #a56f6f;
  }

  textarea:focus {
    border: 1px solid #a56f6f;
    background-color: #cee0979f;
  }
  input {
    width: 96.2%;
    border-top: none;
    border-width: none;
    border-bottom: 2px double #a56f6f;
    background-color: #cee0979f;
  }
  input:focus {
    border: none;
  }
</style>
