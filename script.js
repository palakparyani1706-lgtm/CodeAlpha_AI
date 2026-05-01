async function translateText() {
    const text = document.getElementById("inputText").value;
    const source = document.getElementById("sourceLang").value;
    const target = document.getElementById("targetLang").value;

    const outputBox = document.getElementById("output");

    // empty input check
    if (text.trim() === "") {
        outputBox.innerText = "Please enter text";
        return;
    }

    // same language check
    if (source === target) {
        outputBox.innerText = text;
        return;
    }

    const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=${source}|${target}`;

    // loading state
    outputBox.innerText = "Translating... ⏳";

    try {
        const response = await fetch(url);
        const data = await response.json();

        const result = data?.responseData?.translatedText;

        if (!result) {
            outputBox.innerText = "Translation not available. Try again.";
            return;
        }

        outputBox.innerText = result;
    } 
    catch (error) {
        console.log(error);
        outputBox.innerText = "Error: Check internet or API issue.";
    }
}

function copyText() {
    const output = document.getElementById("output").innerText;

    if (!output || output === "Translating... ⏳") {
        alert("Nothing to copy!");
        return;
    }

    navigator.clipboard.writeText(output);
    alert("Copied to clipboard!");
}