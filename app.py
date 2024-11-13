# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route('/')
def home():
    return render_template('index.html')

class RecipeGenerator:
    def __init__(self):
        self.model = model

        # app.py
    def generate_recipe(self, ingredients, preferences, allergies, cookingTime, difficulty, cuisine):
        prompt = f"""Create a recipe using these ingredients: {ingredients}
        Dietary preferences: {preferences}
        Allergies to avoid: {allergies}
        Cooking time: {cookingTime}
        Difficulty level: {difficulty}
        Cuisine type: {cuisine}
        
        Format the response in markdown with:
        # Recipe Title
        ## Overview
        - Cuisine: {cuisine}
        - Cooking Time: {cookingTime}
        - Difficulty: {difficulty}
        
        ## Ingredients
        - ingredient 1
        - ingredient 2
        
        ## Instructions
        1. Step 1
        2. Step 2
        
        ## Nutritional Info
        * Calories:
        * Protein:
        * Carbs:
        """
        
        response = self.model.generate_content(prompt)
        html_content = markdown2.markdown(response.text)
        return html_content
    
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    generator = RecipeGenerator()
    recipe_html = generator.generate_recipe(
        data['ingredients'],
        data['preferences'],
        data['allergies'],
        data['cookingTime'],
        data['difficulty'],
        data['cuisine']
    )
    return jsonify({'recipe': recipe_html})
    
if __name__ == '__main__':
    app.run(debug=True)