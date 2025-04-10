from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models.functions import Lower
from .models import Recipe, Ingredient, Instruction

class InstructionsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='maximal'))
    class Meta:
        model = Instruction
        fields = ['title', 'content']

class RecipeForm(forms.ModelForm):
    instructions = forms.CharField(widget=CKEditorWidget(config_name='maximal'))
    meal_type = forms.ChoiceField(
        choices=[
            ('breakfast', 'Breakfast'),
            ('lunch', 'Lunch'),
            ('dinner', 'Dinner'),
            ('dessert', 'Dessert'),
        ],
        widget=forms.Select()
    )

    class Meta:
        model = Recipe
        fields = ['title', 'meal_type', 'instructions', 'ingredients']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredients'].queryset = Ingredient.objects.all().order_by(Lower('name'))

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
