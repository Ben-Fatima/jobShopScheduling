const $input = document.getElementById("input");
const $result = document.getElementById("result");
const $solveBtn = document.getElementById("solve");

async function solve() {
  const res = await fetch(`/solve?data=${getInput()}`);
  const data = await res.text();
  const size = data.split(" ").length;
  result.innerHTML += `
    <div class="flex flex-row my-4">
      <p class="bg-blue-700 text-white p-4 rounded-lg mr-4 shadow">
        ${size}
      </p>
      <div class="bg-white py-2 px-4 rounded-lg flex-grow shadow">
        ${data}
      </div>
    </div>
  `;
}

function getInput() {
  let lines = $input.value.split("\n");
  lines = lines.filter((x) => x.trim().length > 0);
  const text = lines.join("\n");
  return btoa(text);
}

$solveBtn.addEventListener("click", solve); 