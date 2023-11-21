<script lang="ts">
  import TextInputOutput from './lib/TextInputOutput.svelte'
  import { translate } from './functions/translate.ts'

  let textToTranslate: string = ''
  let translatedText: string = ''

  const handlePress = async () => {
    translatedText = await translate(textToTranslate)
  }

  const handleKeyDown = async (event: KeyboardEvent) => {
    if (event.key === 'Enter' && event.target === document.body) {
      event.preventDefault();
      await handlePress();
    }
  }
</script>

<svelte:window on:keydown={handleKeyDown} />

<main>
  <h1>Bienvenido a Gerigoncionator®</h1>
  <h3>Ingresa cualquier texto en español, presiona 'Gerigoncify!' y listo! </h3>
  <div class="card">
    <TextInputOutput bind:text={textToTranslate}/>
  </div>

  <button
    on:click={handlePress}>
    Gerigoncify!
  </button>

  <div class="card">
    <TextInputOutput bind:text={translatedText} readonly={true}/>
  </div>

  <img src="./src/assets/oldComputer.png" alt="Old Computer" id="old-computer-image">

</main>



<style>
  @keyframes spinAndPulse {
    0% { transform: scale(1) rotate(0deg); }
    25% { transform: scale(1) rotate(360deg); }
    50% { transform: scale(1.3) rotate(360deg); }
    75% { transform: scale(1) rotate(360deg); }
    100% { transform: scale(1) rotate(360deg); }
  }

  button {
    animation: spinAndPulse 2s infinite;
  }

  #old-computer-image {
    position: absolute; /* Position the image absolutely */
    top: 5%;            /* 0px from the top */
    right: 0;           /* 0px from the left */
    width: 20%;      /* Adjust as needed */
    height: auto;      /* Maintain aspect ratio */
    rotate: 10deg;
  }
</style>