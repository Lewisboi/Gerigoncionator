<script>
  export let text = '';
  export let readonly = false;
</script>

<textarea bind:value={text} {readonly} rows="30" cols="50"/>

<style>
  textarea {
      /* Add your styles here */
      width: 100%;
      height: 200px;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
      background-color: #e6e4e4;
      color: black;
  }
</style>
