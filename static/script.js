// static/script.js
async function generateRecipe() {
    const button = document.querySelector('.generate-btn');
    const spinner = document.querySelector('.loading-spinner');
    
    button.disabled = true;
    spinner.style.display = 'block';

    const ingredients = document.getElementById('ingredients').value;
    const preferences = document.getElementById('preferences').value;
    const allergies = document.getElementById('allergies').value;
    const cookingTime = document.getElementById('cookingTime').value;
    const difficulty = document.getElementById('difficulty').value;
    const cuisine = document.getElementById('cuisine').value;

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ingredients,
                preferences,
                allergies,
                cookingTime,
                difficulty,
                cuisine
            })
        });

        const data = await response.json();
        document.getElementById('recipe-output').innerHTML = data.recipe;
    } catch (error) {
        console.error('Error:', error);
    } finally {
        button.disabled = false;
        spinner.style.display = 'none';
    }
}