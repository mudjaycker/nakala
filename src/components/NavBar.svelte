<script lang="ts">
  let count: number = 0;
  const increment = () => {
    count += 1;
  };
</script>

<section>
  <nav>
    <button> Add reminder </button>
    <button> Reminder list </button>
  </nav>
</section>

<style>
  nav {
    background: var(--color1);
    display: flex;
    justify-content: space-between;
  }
  button{
    all: unset;
    background-color: rgb(255, 208, 0);
    color: var(--color3);
    padding: 1%;
    font-size: 0.8em;
    text-align: center;
    width: 35%;
    font-weight: bold;
 }
  button:hover{
    background-color: var(--color3);
    color: white;
  }


</style>
