
// Current language
let language = "en";

const languageBtn = document.getElementById("languageBtn");
const chatInput = document.getElementById("chatInput");
const chatWindow = document.getElementById("chatWindow");


// English and Roman Urdu language switching
languageBtn.addEventListener("click", () => {

    language = language === "en" ? "ur" : "en";

    // Keep the website left-to-right
    document.documentElement.lang = "en";
    document.documentElement.dir = "ltr";

    document.body.classList.remove("urdu");

    // Update all translated website content
    document.querySelectorAll("[data-en][data-ur]").forEach(element => {
        element.textContent = element.dataset[language];
    });

    // Update language button
    languageBtn.textContent =
        language === "en" ? "Roman Urdu" : "English";

    // Update chatbot placeholder
    chatInput.placeholder =
        language === "en"
            ? "Ask a tourism question..."
            : "Tourism ke bare mein sawal karein...";
});


// AI Tourism Chatbot
document.getElementById("chatForm").addEventListener("submit", async (e) => {

    e.preventDefault();

    const message = chatInput.value.trim();

    if (!message) return;

    const user = document.createElement("div");
    user.className = "user-message";
    user.textContent = message;

    chatWindow.appendChild(user);

    chatInput.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {

        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                language: language
            })
        });

        const data = await response.json();

        const bot = document.createElement("div");
        bot.className = "bot-message";
        bot.textContent = data.reply ||
            "Sorry, no response was returned.";

        chatWindow.appendChild(bot);
        chatWindow.scrollTop = chatWindow.scrollHeight;

    } catch (error) {

        const bot = document.createElement("div");
        bot.className = "bot-message";

        bot.textContent = language === "en"
            ? "Could not connect to the server. Please try again."
            : "Server se connection nahi ho saka. Dobara koshish karein.";

        chatWindow.appendChild(bot);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});


// Smart Trip Planner
document.getElementById("plannerForm").addEventListener("submit", async (e) => {

    e.preventDefault();

    const destination =
        document.getElementById("destinationSelect").value;

    const days =
        document.getElementById("daysSelect").value;

    const interests = [
        ...document.querySelectorAll(".interest-list input:checked")
    ].map(input => input.value);

    const box = document.getElementById("itineraryResult");

    box.textContent = language === "en"
        ? "Preparing suggested itinerary..."
        : "Aap ke safar ka mansuba tayar ho raha hai...";

    try {

        const response = await fetch("/api/itinerary", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                destination,
                days,
                interests,
                language
            })
        });

        const data = await response.json();

        box.replaceChildren();

        if (data.error) {
            box.textContent = data.error;
            return;
        }

        const heading = document.createElement("strong");

        heading.textContent =
            `${data.destination} • ${data.days.length} day(s)`;

        box.appendChild(heading);

        data.days.forEach(day => {

            const paragraph = document.createElement("p");
            paragraph.textContent = day;

            box.appendChild(paragraph);
        });

        const note = document.createElement("small");
        note.textContent = data.disclaimer;

        box.appendChild(note);

    } catch (error) {

        box.textContent = language === "en"
            ? "Could not generate your itinerary. Please try again."
            : "Safar ka mansuba nahi ban saka. Dobara koshish karein.";
    }
});


// Personalized Destination Recommendations
document.getElementById("recommendBtn").addEventListener("click", async () => {

    const interests = [
        ...document.querySelectorAll(".interest-list input:checked")
    ].map(input => input.value);

    const result = document.getElementById("recommendResult");

    result.textContent = language === "en"
        ? "Finding destinations for you..."
        : "Aap ke liye maqamat dhoonde ja rahe hain...";

    try {

        const response = await fetch("/api/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                interests: interests
            })
        });

        const places = await response.json();

        result.replaceChildren();

        places.forEach(place => {

            const card = document.createElement("article");

            const title = document.createElement("h3");
            title.textContent = place.name;

            const description = document.createElement("p");

            description.textContent =
                language === "ur"
                    ? place.roman_description || place.description
                    : place.description;

            const region = document.createElement("small");
            region.textContent = place.region;

            card.append(title, description, region);
            result.appendChild(card);
        });

    } catch (error) {

        result.textContent = language === "en"
            ? "Could not load recommendations. Please try again."
            : "Maqamat suggest nahi ho sake. Dobara koshish karein.";
    }
});


// Register the Progressive Web App service worker
if ("serviceWorker" in navigator) {

    window.addEventListener("load", () => {

        navigator.serviceWorker
            .register("/sw.js")
            .then((registration) => {

                console.log(
                    "Service Worker registered successfully:",
                    registration.scope
                );

            })
            .catch((error) => {

                console.error(
                    "Service Worker registration failed:",
                    error
                );

            });
    });
}
