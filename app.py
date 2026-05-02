from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/verification')
def verification():
    return render_template('verification.html')

@app.route('/polling')
def polling():
    return render_template('polling.html')

@app.route('/simulator', methods=['GET', 'POST'])
def simulator():
    scenario_data = None
    if request.method == 'POST':
        issue = request.form.get('issue')
        
        # Simple logic to define the flow chart based on the issue
        if issue == 'lost_id':
            scenario_data = """
            graph TD
                A[Arrive at Polling Station] --> B{Have Voter Slip?}
                B -- Yes --> C[Present Alternative ID]
                C --> D[Verification by Polling Officer]
                D --> E[Cast Vote]
                B -- No --> F[Check Electoral Roll online or with Booth Level Officer]
                F --> C
            """
        elif issue == 'wrong_booth':
            scenario_data = """
            graph TD
                A[Arrive at Polling Station] --> B{Name on this booth's list?}
                B -- No --> C[Ask Polling Staff / Volunteers]
                C --> D[Check Voter Helpline App / NVSP portal]
                D --> E[Find Correct Booth Part Number]
                E --> F[Travel to Correct Booth]
                F --> G[Verification]
                G --> H[Cast Vote]
                B -- Yes --> G
            """
        elif issue == 'name_missing':
            scenario_data = """
            graph TD
                A[Arrive at Polling Station] --> B{Name on Electoral Roll?}
                B -- No --> C[Show registration confirmation/Form 6 receipt]
                C --> D[If not processed, you cannot vote this time]
                C --> E[Submit Form 6 again for next election]
            """
        else:
            scenario_data = """
            graph TD
                A[Arrive at Polling Station] --> B[Present ID & Voter Slip]
                B --> C[Verification by Polling Officer]
                C --> D[Index Finger Inked]
                D --> E[Sign Register]
                E --> F[Proceed to EVM]
                F --> G[Cast Vote]
                G --> H[Verify VVPAT Slip]
                H --> I[Leave Polling Station]
            """

    return render_template('simulator.html', scenario_data=scenario_data)

if __name__ == '__main__':
    app.run(debug=True)
