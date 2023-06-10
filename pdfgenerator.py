import pdfgen

options = {
    'scale': 2.0,
    'format': 'Letter',
    'margin': {
        'top': '1 in',
        'right': '1 in',
        'bottom': '1 in',
        'left': '1 in',
    },
    
    
}


# Example usage
text = """
<!DOCTYPE html> <html> <head> <title>Legal Framework of Wage and Salary Administration</title> </head> <body> <h1>Legal Framework of Wage and Salary Administration</h1> <h2>Questions and Answers</h2> <ol> <li> <h3>What is the concept of need-based minimum wage?</h3> <p>The concept of need-based minimum wage ensures the minimum human needs of the industrial worker, irrespective of any other considerations.</p> </li> <li> <h3>What is the living wage?</h3> <p>The living wage is the wage that will maintain the workmen in the highest state of industrial efficiency, which will enable him to provide his family with all the material things which are needed for their health and physical well-being, enough to enable him to qualify to discharge his duties as a citizen.</p> </li> <li> <h3>What are the common elements of wages in all the statutory definitions?</h3> <p>The common elements of wages in all the statutory definitions include foodgrains or other articles, any travelling concession, and it does not include any bonus, any contribution paid or payable by the employer to any pension fund or provident fund or for the benefit of the workman under any law for the time being in force, and any gratuity payable on the termination of his service.</p> </li> <li> <h3>What is the difference between minimum wage and need-based minimum wage?</h3> <p>The minimum wage is the wage that is fixed by the authorities concerned, while the need-based minimum wage is the wage that ensures the minimum human needs of the industrial worker, irrespective of any other considerations.</p> </li> <li> <h3>Has the Constitution provided for securing living wage workers?</h3> <p>The Constitution has not provided for securing living wage workers.</p> </li> <li> <h3>What are the six broad categories of wages?</h3> <p>The six broad categories of wages include statutory minimum wage, bare subsistence or minimum wage, living wage, fair wage, minimum wage, and need-based minimum wage.</p> </li> <li> <h3>What is the statutory minimum wage?</h3> <p>The statutory minimum wage is determined according to the provisions of the Minimum Wages Act, 1948.</p> </li> <li> <h3>What is the Fair wage?</h3> <p>The Fair wage is the wage that is based on a fair return on the capital invested in the business, including a reasonable share of profits in proportion to the capital invested.</p> </li> <li> <h3>What is the Minimum wage?</h3> <p>The minimum wage is the wage that is fixed by the authorities concerned for any area for houses provided under the subsidized industrial housing scheme for low-income groups.</p> </li> <li> <h3>What is the Fuel, lighting, and other miscellaneous items of expenditure?</h3> <p>The fuel, lighting, and other miscellaneous items of expenditure should constitute 20% of the total minimum wage.</p> </li> </ol> </body> </html>
"""

pdfgen.sync.from_string(text, 'out.pdf')
