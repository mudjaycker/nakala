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

</style>
