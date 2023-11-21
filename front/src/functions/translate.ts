export async function translate(text: string) {
  const URL = `${import.meta.env.VITE_BACKEND_URL}/gerigoncify`;
  const body = { text };
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  };

  let response = fetch(URL, options);
  let data = await response;
  let jsonData = await data.json();
  return jsonData.gerigoncified;
}