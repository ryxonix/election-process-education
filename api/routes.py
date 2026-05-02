from flask import Blueprint, render_template, request
from core.election_logic import ElectionLogicEngine
from core.guardrails import SemanticInterceptor

api_bp = Blueprint('api', __name__, template_folder='../ui/templates')
logic_engine = ElectionLogicEngine()
interceptor = SemanticInterceptor()

@api_bp.route('/')
def index():
    return render_template('index.html')

@api_bp.route('/registration')
def registration():
    return render_template('registration.html')

@api_bp.route('/verification')
def verification():
    return render_template('verification.html')

@api_bp.route('/polling')
def polling():
    return render_template('polling.html')

@api_bp.route('/simulator', methods=['GET', 'POST'])
def simulator():
    scenario_data = None
    override_msg = None
    procedure_steps = None
    selected_issue = None

    if request.method == 'POST':
        issue = request.form.get('issue', 'normal')
        custom_query = request.form.get('custom_query', '')
        selected_issue = issue

        sanitization_result = interceptor.sanitize(custom_query)
        if not sanitization_result['is_safe']:
            override_msg = sanitization_result['override_message']
            scenario_data = logic_engine.evaluate_scenario('normal')
            procedure_steps = logic_engine.get_procedure_text('normal')
        else:
            scenario_data = logic_engine.evaluate_scenario(issue)
            procedure_steps = logic_engine.get_procedure_text(issue)

    return render_template(
        'simulator.html',
        scenario_data=scenario_data,
        override_msg=override_msg,
        procedure_steps=procedure_steps,
        selected_issue=selected_issue
    )

@api_bp.route('/sandbox', methods=['GET', 'POST'])
def sandbox():
    """Polling Sandbox: Roleplay 'booth friction' scenarios."""
    result = None
    if request.method == 'POST':
        action = request.form.get('action')
        responses = {
            'argue': {
                'outcome': 'fail',
                'msg': "Arguing with the Polling Officer can lead to your removal from the booth. Stay calm.",
                'tip': "The correct action is to politely request the Presiding Officer."
            },
            'presiding_officer': {
                'outcome': 'success',
                'msg': "Correct! The Presiding Officer is the highest authority inside a polling booth.",
                'tip': "The Presiding Officer can verify your name in the supplementary roll or issue a Tender Vote."
            },
            'tender_vote': {
                'outcome': 'success',
                'msg': "Excellent! Exercising your right to a Tender Vote under the RPA 1951 is the proper legal recourse.",
                'tip': "Your Tender Ballot is kept separately and can be counted if the result is disputed."
            },
            'leave': {
                'outcome': 'fail',
                'msg': "Leaving means your vote is lost for this election.",
                'tip': "You have legal rights as a voter. Always escalate to the Presiding Officer first."
            }
        }
        result = responses.get(action, {'outcome': 'fail', 'msg': 'Unknown action.', 'tip': ''})
    return render_template('sandbox.html', result=result)
