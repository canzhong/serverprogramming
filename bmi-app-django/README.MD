Demonstrated basic django web app functionalities. The following task was implemented.

Create a Django application that presents a form prompting the user for name, weight in pounds, and height in feet and inches. When the form is submitted the application returns a page displaying a message with the body mass index (BMI) for that height and weight ("Tim's BMI is 22.7"), as well as a link back to the original page. Calculate BMI as 703*H / (W*W). However, if the input values are invalid (non-numeric, negative) it instead displays an error page containing a relevant message ("height cannot be 'squirrel'" or "inches cannot be -5") and a link back to the original page. 

Helpful BMI sites:

https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php (Links to an external site.)Links to an external site. 

https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm (Links to an external site.)Links to an external site. 

Non-functional requirements

You must use a class-based view for this application. Both the initial form and the response should use the same route: get requests return the form, post requests the response. You should use an if statements in the post method to render different templates for normal responses and error responses. In the normal response template {{name}} and {{bmi}} must be used as template variables.
