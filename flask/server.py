from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from decimal import Decimal   # For currency formatting

JOB_TITLES = ['Software Engineer', 'QA Engineer', 'Product Manager']
JOB_VARIABLES = {'-'.join(title.lower().split()): title for title in JOB_TITLES}  # JOB_VARIABLES['qa-engineer'] = 'QA Engineer'
# JOB_VARIABLES is a dictionary with keys to be submitted from HTML forms, and values the actual text.
# Pause: 1 hour Saturday evening.


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# def currency_format(input_string):    #Designed for strings with no commas.  Number form strips the commas.
#     if input_string[-3:] == '.00':
#         whole_dollars = input_string[:-3]
#     elif '.' not in input_string:
#         whole_dollars = input_string
#     else:
#         return input_string  # If not given in format X.00 or X, give up.

#     trailing_zeroes = ''
#     while whole_dollars[-3:] == '000':   # Remove last three 0s, put comma.
#         trailing_zeroes += ',000'
#         whole_dollars = whole_dollars[:-3]
#     return whole_dollars + trailing_zeroes + '.00'
#  oops, I read the instructions again and saw I should look this up.  The formatting is better than my code.


# YOUR ROUTES GO HERE

@app.route('/')
def index():
    return render_template("index.html", job_titles=JOB_TITLES)


@app.route('/application')
def intake_application():
    return render_template("application-form.html", jobs=JOB_VARIABLES)


@app.route('/application/success', methods=["POST"])
def process_application():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    min_salary = request.form.get('min-salary', '0')    # Optional field
    job_title_key = request.form.get('job-title')       # e.g. 'product-manager'
    job_title = JOB_VARIABLES.get(job_title_key)           # e.g. 'Product Manager'
    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           job_title=job_title,
                           min_salary='${:,.2f}'.format(Decimal(min_salary))
                           )


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
