<script>
  let reminder = {
    title: "",
    text: "",
  };
  $: save = function () {
    let string = JSON.stringify(reminder);
    localStorage.setItem("reminder", string);
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
    margin-top: 20%;
    margin-left: 10%;
    padding: 10%;
  }
  textarea {
    width: 90%;
    margin-top: 2%;
  }
  input {
    width: 90%;
  }
</style>
